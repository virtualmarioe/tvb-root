# -*- coding: utf-8 -*-
#
#
#  TheVirtualBrain-Scientific Package. This package holds all simulators, and 
# analysers necessary to run brain-simulations. You can use it stand alone or
# in conjunction with TheVirtualBrain-Framework Package. See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2020, Baycrest Centre for Geriatric Care ("Baycrest") and others
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this
# program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#   CITATION:
# When using The Virtual Brain for scientific publications, please cite it as follows:
#
#   Paula Sanz Leon, Stuart A. Knock, M. Marmaduke Woodman, Lia Domide,
#   Jochen Mersmann, Anthony R. McIntosh, Viktor Jirsa (2013)
#       The Virtual Brain: a simulator of primate brain network dynamics.
#   Frontiers in Neuroinformatics (7:10. doi: 10.3389/fninf.2013.00010)
#
#

"""
Filler analyzer: Takes a TimeSeries object and returns a Float.

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa@codemart.ro>
.. moduleauthor:: Stuart A. Knock <Stuart@tvb.invalid>

"""

import tvb.analyzers.metrics_base as metrics_base


class VarianceNodeVariance(metrics_base.BaseTimeseriesMetricAlgorithm):
    """
    Zero-centres all the time-series, calculates the variance for each node 
    time-series and returns the variance of the node variances. 

    Input:
    TimeSeries DataType
    
    Output: 
    Float
    
    This is a crude indicator of how different the "excitability" of the model is
    from node to node.
    """

    def evaluate(self):
        """
        Compute the zero centered variance of node variances for the time_series.
        """

        shape = self.time_series.data.shape
        tpts = shape[0]

        if self.start_point != 0.0:
            start_tpt = self.start_point / self.time_series.sample_period
            self.log.debug("Will discard: %s time points" % start_tpt)
        else:
            start_tpt = 0

        if start_tpt > tpts:
            self.log.warning("The time-series is shorter than the starting point")
            self.log.debug("Will divide the time-series into %d segments." % self.segment)
            # Lazy strategy
            start_tpt = int((self.segment - 1) * (tpts // self.segment))

        start_tpt = int(start_tpt)
        zero_mean_data = (self.time_series.data[start_tpt:, :] - self.time_series.data[start_tpt:, :].mean(axis=0))
        # reshape by concatenating the time-series of each var and modes for each node.
        zero_mean_data = zero_mean_data.transpose((0, 1, 3, 2))
        cat_tpts = zero_mean_data.shape[0] * shape[1] * shape[3]
        zero_mean_data = zero_mean_data.reshape((cat_tpts, shape[2]), order="F")
        # Variance over time-points, state-variables, and modes for each node.
        node_variance = zero_mean_data.var(axis=0)
        # Variance of that variance over nodes
        result = node_variance.var()
        return result
