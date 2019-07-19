#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2ORandomForestEstimator(H2OEstimator):
    """
    Distributed Random Forest

    """

    algo = "drf"

    def __init__(self, **kwargs):
        super(H2ORandomForestEstimator, self).__init__()
        self._parms = {}
        names_list = {"model_id", "training_frame", "validation_frame", "nfolds", "keep_cross_validation_models",
                      "keep_cross_validation_predictions", "keep_cross_validation_fold_assignment",
                      "score_each_iteration", "score_tree_interval", "fold_assignment", "fold_column",
                      "response_column", "ignored_columns", "ignore_const_cols", "offset_column", "weights_column",
                      "balance_classes", "class_sampling_factors", "max_after_balance_size",
                      "max_confusion_matrix_size", "max_hit_ratio_k", "ntrees", "max_depth", "min_rows", "nbins",
                      "nbins_top_level", "nbins_cats", "r2_stopping", "stopping_rounds", "stopping_metric",
                      "stopping_tolerance", "max_runtime_secs", "seed", "build_tree_one_node", "mtries", "sample_rate",
                      "sample_rate_per_class", "binomial_double_trees", "checkpoint",
                      "col_sample_rate_change_per_level", "col_sample_rate_per_tree", "min_split_improvement",
                      "histogram_type", "categorical_encoding", "calibrate_model", "calibration_frame", "distribution",
                      "custom_metric_func", "export_checkpoints_dir", "check_constant_response"}
        if "Lambda" in kwargs: kwargs["lambda_"] = kwargs.pop("Lambda")
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in names_list:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``H2OFrame``.
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')


    @property
    def validation_frame(self):
        """
        Id of the validation data frame.

        Type: ``H2OFrame``.
        """
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        self._parms["validation_frame"] = H2OFrame._validate(validation_frame, 'validation_frame')


    @property
    def nfolds(self):
        """
        Number of folds for K-fold cross-validation (0 to disable or >= 2).

        Type: ``int``  (default: ``0``).
        """
        return self._parms.get("nfolds")

    @nfolds.setter
    def nfolds(self, nfolds):
        assert_is_type(nfolds, None, int)
        self._parms["nfolds"] = nfolds


    @property
    def keep_cross_validation_models(self):
        """
        Whether to keep the cross-validation models.

        Type: ``bool``  (default: ``True``).
        """
        return self._parms.get("keep_cross_validation_models")

    @keep_cross_validation_models.setter
    def keep_cross_validation_models(self, keep_cross_validation_models):
        assert_is_type(keep_cross_validation_models, None, bool)
        self._parms["keep_cross_validation_models"] = keep_cross_validation_models


    @property
    def keep_cross_validation_predictions(self):
        """
        Whether to keep the predictions of the cross-validation models.

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("keep_cross_validation_predictions")

    @keep_cross_validation_predictions.setter
    def keep_cross_validation_predictions(self, keep_cross_validation_predictions):
        assert_is_type(keep_cross_validation_predictions, None, bool)
        self._parms["keep_cross_validation_predictions"] = keep_cross_validation_predictions


    @property
    def keep_cross_validation_fold_assignment(self):
        """
        Whether to keep the cross-validation fold assignment.

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("keep_cross_validation_fold_assignment")

    @keep_cross_validation_fold_assignment.setter
    def keep_cross_validation_fold_assignment(self, keep_cross_validation_fold_assignment):
        assert_is_type(keep_cross_validation_fold_assignment, None, bool)
        self._parms["keep_cross_validation_fold_assignment"] = keep_cross_validation_fold_assignment


    @property
    def score_each_iteration(self):
        """
        Whether to score during each iteration of model training.

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration


    @property
    def score_tree_interval(self):
        """
        Score the model after every so many trees. Disabled if set to 0.

        Type: ``int``  (default: ``0``).
        """
        return self._parms.get("score_tree_interval")

    @score_tree_interval.setter
    def score_tree_interval(self, score_tree_interval):
        assert_is_type(score_tree_interval, None, int)
        self._parms["score_tree_interval"] = score_tree_interval


    @property
    def fold_assignment(self):
        """
        Cross-validation fold assignment scheme, if fold_column is not specified. The 'Stratified' option will stratify
        the folds based on the response variable, for classification problems.

        One of: ``"auto"``, ``"random"``, ``"modulo"``, ``"stratified"``  (default: ``"auto"``).
        """
        return self._parms.get("fold_assignment")

    @fold_assignment.setter
    def fold_assignment(self, fold_assignment):
        assert_is_type(fold_assignment, None, Enum("auto", "random", "modulo", "stratified"))
        self._parms["fold_assignment"] = fold_assignment


    @property
    def fold_column(self):
        """
        Column with cross-validation fold index assignment per observation.

        Type: ``str``.
        """
        return self._parms.get("fold_column")

    @fold_column.setter
    def fold_column(self, fold_column):
        assert_is_type(fold_column, None, str)
        self._parms["fold_column"] = fold_column


    @property
    def response_column(self):
        """
        Response variable column.

        Type: ``str``.
        """
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column


    @property
    def ignored_columns(self):
        """
        Names of columns to ignore for training.

        Type: ``List[str]``.
        """
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def ignore_const_cols(self):
        """
        Ignore constant columns.

        Type: ``bool``  (default: ``True``).
        """
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def offset_column(self):
        """
        [Deprecated] Offset column. This will be added to the combination of columns before applying the link function.

        Type: ``str``.
        """
        return self._parms.get("offset_column")

    @offset_column.setter
    def offset_column(self, offset_column):
        assert_is_type(offset_column, None, str)
        self._parms["offset_column"] = offset_column


    @property
    def weights_column(self):
        """
        Column with observation weights. Giving some observation a weight of zero is equivalent to excluding it from the
        dataset; giving an observation a relative weight of 2 is equivalent to repeating that row twice. Negative
        weights are not allowed. Note: Weights are per-row observation weights and do not increase the size of the data
        frame. This is typically the number of times a row is repeated, but non-integer values are supported as well.
        During training, rows with higher weights matter more, due to the larger loss function pre-factor.

        Type: ``str``.
        """
        return self._parms.get("weights_column")

    @weights_column.setter
    def weights_column(self, weights_column):
        assert_is_type(weights_column, None, str)
        self._parms["weights_column"] = weights_column


    @property
    def balance_classes(self):
        """
        Balance training data class counts via over/under-sampling (for imbalanced data).

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("balance_classes")

    @balance_classes.setter
    def balance_classes(self, balance_classes):
        assert_is_type(balance_classes, None, bool)
        self._parms["balance_classes"] = balance_classes


    @property
    def class_sampling_factors(self):
        """
        Desired over/under-sampling ratios per class (in lexicographic order). If not specified, sampling factors will
        be automatically computed to obtain class balance during training. Requires balance_classes.

        Type: ``List[float]``.
        """
        return self._parms.get("class_sampling_factors")

    @class_sampling_factors.setter
    def class_sampling_factors(self, class_sampling_factors):
        assert_is_type(class_sampling_factors, None, [float])
        self._parms["class_sampling_factors"] = class_sampling_factors


    @property
    def max_after_balance_size(self):
        """
        Maximum relative size of the training data after balancing class counts (can be less than 1.0). Requires
        balance_classes.

        Type: ``float``  (default: ``5``).
        """
        return self._parms.get("max_after_balance_size")

    @max_after_balance_size.setter
    def max_after_balance_size(self, max_after_balance_size):
        assert_is_type(max_after_balance_size, None, float)
        self._parms["max_after_balance_size"] = max_after_balance_size


    @property
    def max_confusion_matrix_size(self):
        """
        [Deprecated] Maximum size (# classes) for confusion matrices to be printed in the Logs

        Type: ``int``  (default: ``20``).
        """
        return self._parms.get("max_confusion_matrix_size")

    @max_confusion_matrix_size.setter
    def max_confusion_matrix_size(self, max_confusion_matrix_size):
        assert_is_type(max_confusion_matrix_size, None, int)
        self._parms["max_confusion_matrix_size"] = max_confusion_matrix_size


    @property
    def max_hit_ratio_k(self):
        """
        Max. number (top K) of predictions to use for hit ratio computation (for multi-class only, 0 to disable)

        Type: ``int``  (default: ``0``).
        """
        return self._parms.get("max_hit_ratio_k")

    @max_hit_ratio_k.setter
    def max_hit_ratio_k(self, max_hit_ratio_k):
        assert_is_type(max_hit_ratio_k, None, int)
        self._parms["max_hit_ratio_k"] = max_hit_ratio_k


    @property
    def ntrees(self):
        """
        Number of trees.

        Type: ``int``  (default: ``50``).
        """
        return self._parms.get("ntrees")

    @ntrees.setter
    def ntrees(self, ntrees):
        assert_is_type(ntrees, None, int)
        self._parms["ntrees"] = ntrees


    @property
    def max_depth(self):
        """
        Maximum tree depth.

        Type: ``int``  (default: ``20``).
        """
        return self._parms.get("max_depth")

    @max_depth.setter
    def max_depth(self, max_depth):
        assert_is_type(max_depth, None, int)
        self._parms["max_depth"] = max_depth


    @property
    def min_rows(self):
        """
        Fewest allowed (weighted) observations in a leaf.

        Type: ``float``  (default: ``1``).
        """
        return self._parms.get("min_rows")

    @min_rows.setter
    def min_rows(self, min_rows):
        assert_is_type(min_rows, None, numeric)
        self._parms["min_rows"] = min_rows


    @property
    def nbins(self):
        """
        For numerical columns (real/int), build a histogram of (at least) this many bins, then split at the best point

        Type: ``int``  (default: ``20``).
        """
        return self._parms.get("nbins")

    @nbins.setter
    def nbins(self, nbins):
        assert_is_type(nbins, None, int)
        self._parms["nbins"] = nbins


    @property
    def nbins_top_level(self):
        """
        For numerical columns (real/int), build a histogram of (at most) this many bins at the root level, then decrease
        by factor of two per level

        Type: ``int``  (default: ``1024``).
        """
        return self._parms.get("nbins_top_level")

    @nbins_top_level.setter
    def nbins_top_level(self, nbins_top_level):
        assert_is_type(nbins_top_level, None, int)
        self._parms["nbins_top_level"] = nbins_top_level


    @property
    def nbins_cats(self):
        """
        For categorical columns (factors), build a histogram of this many bins, then split at the best point. Higher
        values can lead to more overfitting.

        Type: ``int``  (default: ``1024``).
        """
        return self._parms.get("nbins_cats")

    @nbins_cats.setter
    def nbins_cats(self, nbins_cats):
        assert_is_type(nbins_cats, None, int)
        self._parms["nbins_cats"] = nbins_cats


    @property
    def r2_stopping(self):
        """
        r2_stopping is no longer supported and will be ignored if set - please use stopping_rounds, stopping_metric and
        stopping_tolerance instead. Previous version of H2O would stop making trees when the R^2 metric equals or
        exceeds this

        Type: ``float``  (default: ``1.797693135e+308``).
        """
        return self._parms.get("r2_stopping")

    @r2_stopping.setter
    def r2_stopping(self, r2_stopping):
        assert_is_type(r2_stopping, None, numeric)
        self._parms["r2_stopping"] = r2_stopping


    @property
    def stopping_rounds(self):
        """
        Early stopping based on convergence of stopping_metric. Stop if simple moving average of length k of the
        stopping_metric does not improve for k:=stopping_rounds scoring events (0 to disable)

        Type: ``int``  (default: ``0``).
        """
        return self._parms.get("stopping_rounds")

    @stopping_rounds.setter
    def stopping_rounds(self, stopping_rounds):
        assert_is_type(stopping_rounds, None, int)
        self._parms["stopping_rounds"] = stopping_rounds


    @property
    def stopping_metric(self):
        """
        Metric to use for early stopping (AUTO: logloss for classification, deviance for regression and anonomaly_score
        for Isolation Forest). Note that custom and custom_increasing can only be used in GBM and DRF with the Python
        client.

        One of: ``"auto"``, ``"deviance"``, ``"logloss"``, ``"mse"``, ``"rmse"``, ``"mae"``, ``"rmsle"``, ``"auc"``,
        ``"lift_top_group"``, ``"misclassification"``, ``"mean_per_class_error"``, ``"r2"``, ``"custom"``,
        ``"custom_increasing"``  (default: ``"auto"``).
        """
        return self._parms.get("stopping_metric")

    @stopping_metric.setter
    def stopping_metric(self, stopping_metric):
        assert_is_type(stopping_metric, None, Enum("auto", "deviance", "logloss", "mse", "rmse", "mae", "rmsle", "auc", "lift_top_group", "misclassification", "mean_per_class_error", "r2", "custom", "custom_increasing"))
        self._parms["stopping_metric"] = stopping_metric


    @property
    def stopping_tolerance(self):
        """
        Relative tolerance for metric-based stopping criterion (stop if relative improvement is not at least this much)

        Type: ``float``  (default: ``0.001``).
        """
        return self._parms.get("stopping_tolerance")

    @stopping_tolerance.setter
    def stopping_tolerance(self, stopping_tolerance):
        assert_is_type(stopping_tolerance, None, numeric)
        self._parms["stopping_tolerance"] = stopping_tolerance


    @property
    def max_runtime_secs(self):
        """
        Maximum allowed runtime in seconds for model training. Use 0 to disable.

        Type: ``float``  (default: ``0``).
        """
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs


    @property
    def seed(self):
        """
        Seed for pseudo random number generator (if applicable)

        Type: ``int``  (default: ``-1``).
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed


    @property
    def build_tree_one_node(self):
        """
        Run on one node only; no network overhead but fewer cpus used.  Suitable for small datasets.

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("build_tree_one_node")

    @build_tree_one_node.setter
    def build_tree_one_node(self, build_tree_one_node):
        assert_is_type(build_tree_one_node, None, bool)
        self._parms["build_tree_one_node"] = build_tree_one_node


    @property
    def mtries(self):
        """
        Number of variables randomly sampled as candidates at each split. If set to -1, defaults to sqrt{p} for
        classification and p/3 for regression (where p is the # of predictors

        Type: ``int``  (default: ``-1``).
        """
        return self._parms.get("mtries")

    @mtries.setter
    def mtries(self, mtries):
        assert_is_type(mtries, None, int)
        self._parms["mtries"] = mtries


    @property
    def sample_rate(self):
        """
        Row sample rate per tree (from 0.0 to 1.0)

        Type: ``float``  (default: ``0.6320000291``).
        """
        return self._parms.get("sample_rate")

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        assert_is_type(sample_rate, None, numeric)
        self._parms["sample_rate"] = sample_rate


    @property
    def sample_rate_per_class(self):
        """
        A list of row sample rates per class (relative fraction for each class, from 0.0 to 1.0), for each tree

        Type: ``List[float]``.
        """
        return self._parms.get("sample_rate_per_class")

    @sample_rate_per_class.setter
    def sample_rate_per_class(self, sample_rate_per_class):
        assert_is_type(sample_rate_per_class, None, [numeric])
        self._parms["sample_rate_per_class"] = sample_rate_per_class


    @property
    def binomial_double_trees(self):
        """
        For binary classification: Build 2x as many trees (one per class) - can lead to higher accuracy.

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("binomial_double_trees")

    @binomial_double_trees.setter
    def binomial_double_trees(self, binomial_double_trees):
        assert_is_type(binomial_double_trees, None, bool)
        self._parms["binomial_double_trees"] = binomial_double_trees


    @property
    def checkpoint(self):
        """
        Model checkpoint to resume training with.

        Type: ``str``.
        """
        return self._parms.get("checkpoint")

    @checkpoint.setter
    def checkpoint(self, checkpoint):
        assert_is_type(checkpoint, None, str, H2OEstimator)
        self._parms["checkpoint"] = checkpoint


    @property
    def col_sample_rate_change_per_level(self):
        """
        Relative change of the column sampling rate for every level (must be > 0.0 and <= 2.0)

        Type: ``float``  (default: ``1``).
        """
        return self._parms.get("col_sample_rate_change_per_level")

    @col_sample_rate_change_per_level.setter
    def col_sample_rate_change_per_level(self, col_sample_rate_change_per_level):
        assert_is_type(col_sample_rate_change_per_level, None, numeric)
        self._parms["col_sample_rate_change_per_level"] = col_sample_rate_change_per_level


    @property
    def col_sample_rate_per_tree(self):
        """
        Column sample rate per tree (from 0.0 to 1.0)

        Type: ``float``  (default: ``1``).
        """
        return self._parms.get("col_sample_rate_per_tree")

    @col_sample_rate_per_tree.setter
    def col_sample_rate_per_tree(self, col_sample_rate_per_tree):
        assert_is_type(col_sample_rate_per_tree, None, numeric)
        self._parms["col_sample_rate_per_tree"] = col_sample_rate_per_tree


    @property
    def min_split_improvement(self):
        """
        Minimum relative improvement in squared error reduction for a split to happen

        Type: ``float``  (default: ``1e-05``).
        """
        return self._parms.get("min_split_improvement")

    @min_split_improvement.setter
    def min_split_improvement(self, min_split_improvement):
        assert_is_type(min_split_improvement, None, numeric)
        self._parms["min_split_improvement"] = min_split_improvement


    @property
    def histogram_type(self):
        """
        What type of histogram to use for finding optimal split points

        One of: ``"auto"``, ``"uniform_adaptive"``, ``"random"``, ``"quantiles_global"``, ``"round_robin"``  (default:
        ``"auto"``).
        """
        return self._parms.get("histogram_type")

    @histogram_type.setter
    def histogram_type(self, histogram_type):
        assert_is_type(histogram_type, None, Enum("auto", "uniform_adaptive", "random", "quantiles_global", "round_robin"))
        self._parms["histogram_type"] = histogram_type


    @property
    def categorical_encoding(self):
        """
        Encoding scheme for categorical features

        One of: ``"auto"``, ``"enum"``, ``"one_hot_internal"``, ``"one_hot_explicit"``, ``"binary"``, ``"eigen"``,
        ``"label_encoder"``, ``"sort_by_response"``, ``"enum_limited"``  (default: ``"auto"``).
        """
        return self._parms.get("categorical_encoding")

    @categorical_encoding.setter
    def categorical_encoding(self, categorical_encoding):
        assert_is_type(categorical_encoding, None, Enum("auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder", "sort_by_response", "enum_limited"))
        self._parms["categorical_encoding"] = categorical_encoding


    @property
    def calibrate_model(self):
        """
        Use Platt Scaling to calculate calibrated class probabilities. Calibration can provide more accurate estimates
        of class probabilities.

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("calibrate_model")

    @calibrate_model.setter
    def calibrate_model(self, calibrate_model):
        assert_is_type(calibrate_model, None, bool)
        self._parms["calibrate_model"] = calibrate_model


    @property
    def calibration_frame(self):
        """
        Calibration frame for Platt Scaling

        Type: ``H2OFrame``.
        """
        return self._parms.get("calibration_frame")

    @calibration_frame.setter
    def calibration_frame(self, calibration_frame):
        self._parms["calibration_frame"] = H2OFrame._validate(calibration_frame, 'calibration_frame')


    @property
    def distribution(self):
        """
        [Deprecated] Distribution function

        One of: ``"auto"``, ``"bernoulli"``, ``"multinomial"``, ``"gaussian"``, ``"poisson"``, ``"gamma"``,
        ``"tweedie"``, ``"laplace"``, ``"quantile"``, ``"huber"``  (default: ``"auto"``).
        """
        return self._parms.get("distribution")

    @distribution.setter
    def distribution(self, distribution):
        assert_is_type(distribution, None, Enum("auto", "bernoulli", "multinomial", "gaussian", "poisson", "gamma", "tweedie", "laplace", "quantile", "huber"))
        self._parms["distribution"] = distribution


    @property
    def custom_metric_func(self):
        """
        Reference to custom evaluation function, format: `language:keyName=funcName`

        Type: ``str``.
        """
        return self._parms.get("custom_metric_func")

    @custom_metric_func.setter
    def custom_metric_func(self, custom_metric_func):
        assert_is_type(custom_metric_func, None, str)
        self._parms["custom_metric_func"] = custom_metric_func


    @property
    def export_checkpoints_dir(self):
        """
        Automatically export generated models to this directory.

        Type: ``str``.
        """
        return self._parms.get("export_checkpoints_dir")

    @export_checkpoints_dir.setter
    def export_checkpoints_dir(self, export_checkpoints_dir):
        assert_is_type(export_checkpoints_dir, None, str)
        self._parms["export_checkpoints_dir"] = export_checkpoints_dir


    @property
    def check_constant_response(self):
        """
        Check if response column is constant. If enabled, then an exception is thrown if the response column is a
        constant value.If disabled, then model will train regardless of the response column being a constant value or
        not.

        Type: ``bool``  (default: ``True``).
        """
        return self._parms.get("check_constant_response")

    @check_constant_response.setter
    def check_constant_response(self, check_constant_response):
        assert_is_type(check_constant_response, None, bool)
        self._parms["check_constant_response"] = check_constant_response


