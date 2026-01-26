# Benchopt Benchmark Sprint


We just finished three days of benchmarking sprint with **[`benchopt`](https://benchopt.github.io/)**!! With 40 participants, we had lots of fun, energy and nice achievements, this felt amazing! 🤗

![](https://notes.inria.fr/uploads/upload_f219a04611437737ea3067129f9cf85d.png =300x) <span style="width: 2em; display:inline-block"></span>![](https://notes.inria.fr/uploads/upload_7f40b86f67608f3f3fe8555d8a50e2db.png =300x)

Here are a few takeaways from the feedbacks we got on **[`benchopt`](https://benchopt.github.io/)** and our discussions!


### What is benchopt?

For those of you who haven't heard about it yet, here is a small catch-up:

![Benchopt Logo](https://raw.githubusercontent.com/benchopt/communication_materials/main/posters/images/logo_benchopt.png =400x241)

Benchmarking methods on standard databases are at the heart of the scientific method in ML. Yet, only a few domains systematically use reference benchmarks to showcase the performances of new methods. Even for these benchmarks, reaching the right performances for competitor methods can be challenging and requires a lot of work.

Here enters **[`benchopt`](https://benchopt.github.io/)**! The library gives you the tools to build and execute benchmarks for the ML and optimization communities, making them easy to share, extend, and run fast. First, **[`benchopt`](https://benchopt.github.io/)** provides **a framework template to organize benchmarks**, making every step transparent --*e.g.* how the data is preprocessed, how the metrics are computed, etc. Thanks to their standardized structure, the developed benchmarks are easily extendable, meaning that new datasets and methods can be seamlessly integrated. Second, it ships with **a set of tools to run and process the benchmarks' results** easily -- with parallel run, caching, interactive visualization, ... These tools are usually redesigned for each new benchmark. By sharing them in a common library, we make them more powerful and reliable. Note that this library is not restricted to evaluate Python code, as it can also be used to evaluate solvers in other languages such as Julia or R.

To learn more about **[`benchopt`](https://benchopt.github.io/)**, you can check out our **[NeurIPS 2022 paper](https://arxiv.org/abs/2206.13424)**, which also showcases scientific findings from benchmarking classical ML tasks and algorithms.

### Developing new benchmarks

During this sprint, we developed new benchmarks, gathered feedback, and saw which benchmarking tools were most needed. Most of the participants had never worked with benchopt. Their goal was to create new benchmarks using **[`benchopt`](https://benchopt.github.io/)**, ranging from optimization benchmarks -- *e.g.* training a neural network with `pytorch` or `jax` on image classification -- to more complex workflows -- *e.g.* comparing different fMRI alignment or domain adaptation methods.

Using the **[template benchmark](https://github.com/benchopt/template_benchmark)**, they were all able to quickly get a running benchmark. This template provides the basic code structure for a benchmark, with many comments to help you get started. The feedback helped us improve the template and clarify the processing flow in **[`benchopt`](https://benchopt.github.io/)**, summarized in the following diagram.
<!-- We also improved our diagram describing this flow and clarified the workflow methods' names to better reflect the matching ones: `get_data/set_data`, `get_objective/set_objective` and we will modify `compute` to have `get_result/evaluate_result`. -->


![benchopt workflow diagram](https://raw.githubusercontent.com/benchopt/communication_materials/master/sharedimages/benchopt_schema_dependency.svg "benchopt workflow")


<!-- Following this workflow and the template benchmark, the users can create a benchmark by filling in these seven methods step-by-step. This API creates the glue between the objective, defined in ``objective.py``, and the various datasets and solvers. Each of ``get_XXX``methods returns a dictionary whose keys are passed as keyword arguments to the matching ``set_XXX`` method. The ``run`` function of the solver defines how to call the specific solver for various tolerance or number of iterations. Therefore, **[`benchopt`](https://benchopt.github.io/)** only requires that the methods defined in the benchopt's benchmark are compatible, while each solver and dataset can then have its own way of processing the data internally. This allows us to easily compare methods relying on different frameworks, even when their APIs are not compatible. -->

The onboarding of new users was greatly improved by adding more tutorials and examples, and revamping our documentation -- :pray: big thanks to [Jeremy Cohen](https://jeremy-e-cohen.jimdofree.com/) and [Badr Moufad](https://github.com/Badr-MOUFAD) on this one.
<!-- For instance, checkout out new **[step-by-step tutorial]()**, or our improved description of **[how the performance is assessed with varying computational budget](https://benchopt.github.io/advanced.html#changing-the-strategy-to-grow-the-computational-budget-stop-val)**, which was a source of confusion for some users. -->

<!-- ### Benchmarking for complex tasks

For some benchmarks with complex tasks, defining the scope and the good metrics to track is a challenging process. For instance, the various methods to solve Non-negative Matrix Factorization (NMF) don't optimize the same objective function. The use of one objective function as the metric of choice for the benchmark is therefor not properly evaluating all the methods that use a different criterion. -->

### Major achievement: 14 benchmarks in 3 days!

Our greatest pride is that the participants were all able to produce benchmarks within a few hours! Note that an important aspect of this benchmarking initiative is that the goal is not to re-code the various methods but to aggregate them from the different sources they are available from. This not only allows comparing algorithms but also their implementations in existing frameworks. In the end, **[`benchopt`](https://benchopt.github.io/)** is here to **create the glue to run and aggregate the results** for the developed methods. During this coding sprint, we created or improved many benchmarks:

- **[Simulation Based Inference (SBI)](https://github.com/JuliaLinhart/benchmark_sbi)**: [Julia Linhart](https://www.linkedin.com/in/julia-linhart-70817315b/?original_referer=https%3A%2F%2Fscholar.google.com%2F), [François Rozet](https://francois-rozet.github.io/) and [Matthieu Mouzaoui](https://fr.linkedin.com/in/matthieu-mouzaoui) focused on evaluating Likelihood-free Inference methods from frameworks such as **[`sbi`](https://github.com/mackelab/sbi)** and **[`lampe`](https://github.com/francois-rozet/lampe)**. Produced during the sprint, the following plot shows the negative log-likelihood on a test set for different methods -- FMPE, NPE and NRE -- on simulated data (SLCP), as a function of time.
![](https://notes.inria.fr/uploads/upload_86c5d97827ac708a05911c429a014c1e.png)<br/>
This benchmark builds upon a [previous benchmarking initiative](https://github.com/mackelab/sbim) by the Macke Lab, which is very extensive but hard to extend with methods developed outside the **[`sbi`](https://github.com/mackelab/sbi)** library.

- **[Inverse Problems](https://github.com/matthieutrs/benchmark_deepinv)**: [Matthieu Terris](https://matthieutrs.github.io/), [Pierre-Antoine Comby](https://github.com/paquiteau) and [Chaithya GR](https://chaithyagr.github.io/) compared different approaches to solve inverse problems, with a strong focus on learning-based approaches. In particular, they focussed on MRI reconstruction problems. This benchmark uses the **[deepinv](deepinv.github.io/)** library, which provides a simple API to solve inverse problems with deep learning. The following figures showcase the PSNR of three different methods as a function of the running time, as well as the reconstructed images on the fastMRI dataset. The plot shows that the deep learning-based approach DPIR outperforms both wavelet-based methods in this example.
  ![](https://notes.inria.fr/uploads/upload_cfa50b5f638d1582672640f61496f931.png)
  ![](https://notes.inria.fr/uploads/upload_99e75015f65564dd88c4bc24dcedaabf.png)
  <br/>
  Broader comparisons will be performed on this benchmark, in particular by adding multicoiled datasets.

- **[Brain Computer Interface (BCI)](https://github.com/benchopt/benchmark_bci)**: [Christopher Marouani](https://fr.linkedin.com/in/christopher-marouani-852922245) and [Bruno Aristimunha](https://www.linkedin.com/in/bruaristimunha) provided an easy way to run BCI experiments to compare both Riemmanian and deep-learning methods. It allows running the pipelines developed with the **[`Moabb`](https://neurotechx.github.io/moabb/)** and **[`braindecode`](https://braindecode.org/)** libraries, and to easily add new methods. In particular, we explored how data augmentation can be applied to classical BCI methods, by adding extra augmented samples in the training set. In the following plot, the number of iterations corresponds to the number of times the dataset is augmented. It shows that for some methods such as `TangentSpaceLR`, adding twice as much augmented data in the training set can improve the balanced accuracy.
  ![](https://notes.inria.fr/uploads/upload_10df26e18b1ba79953af60b6bb1631e6.png)
<!--   ![](https://notes.inria.fr/uploads/upload_9f2e31149f3c2afe492c3dfae5788f40.png)<br/> -->
  Extra results with deep learning methods will be added in the next months to complement these preliminary results.

- **[Brain age prediction](https://github.com/apmellot/brain_age_meeg_benchmark)**: [Apolline Mellot](https://scholar.google.com/citations?user=IG5V0YEAAAAJ&hl=en) and [Katia Chardon](https://fr.linkedin.com/in/katiachardon) compared the **[`coffeine`](https://github.com/coffeine-labs/coffeine)** pipelines to predict a healthy subject's age from neuroimaging data. One specificity of the benchmark is that we did not want to compare the performance of the different methods for varying numbers of iterations but with varying numbers of training samples -- as learning curves. The following illustration shows how the MAEs of the methods evolve with the number of training samples.
  ![](https://notes.inria.fr/uploads/upload_f52d334ead161cff7121275d99dc2027.png)<br/>
  This benchmark raised questions about how to deal with datasets where the data cannot be easily downloaded from the internet, but one needs to [specify their location on the system](https://github.com/benchopt/benchopt/issues/627).
  
- **[fMRI alignment](https://github.com/man-shu/fmralign_benchopt)**: when working with fMRI data, it is often necessary to align the data to cope with the position in the scanner and the brain's topology of each individual. [Pierre-Louis Barbarant](https://fr.linkedin.com/in/plbarbarant), [Himanshu Aggarwal](https://github.com/man-shu) and [Bertrand Thirion](https://pages.saclay.inria.fr/bertrand.thirion/) compared the different methods that have been proposed to align such data, by evaluating how such aligned data were improving predictive performance -- decoding capabilities -- of downstream algorithms.
  
- **[Non-negative Matrix Factorization (NMF)](https://github.com/benchopt/benchmark_nmf)**: [Jeremy Cohen](https://jeremy-e-cohen.jimdofree.com/) and [Cassio Fraga Dantas](https://cassiofragadantas.github.io/) added various loss criteria as objective metrics, to compare the methods across criterions. Indeed, the various methods to solve NMF do not optimize the same objective function. The use of one objective function as the metric of choice for the benchmark is therefore not properly evaluating all the methods that use a different criterion. Putting all the possible losses allows us to fairly assess the performance across criterions.

- **[Bilevel optimization](https://github.com/benchopt/benchmark_bilevel)**: this benchmark was originally developed to compare the different bilevel stochastic optimization methods for a [NeurIPS paper](https://arxiv.org/abs/2201.13409). During this sprint, [Mathieu Dagréou](https://matdag.github.io/) and [Pierre Ablin](https://pierreablin.com/) improved the documentation of the benchmark, and added new tasks and solvers, in particular methods based on [`jaxopt`](https://jaxopt.github.io/stable/).
  
- **[Optimal Transport](https://github.com/benchopt/benchmark_ot)**: this benchmark aims to evaluate the different methods to solve Optimal Transport (OT) problems, in particular using three main implementations [POT](https://pythonot.github.io/), [OTT-jax](https://ott-jax.readthedocs.io) and [GeomLoss](https://www.kernel-operations.io/geomloss/). [Jean Feydy](https://www.jeanfeydy.com/), [Marco Cuturi](https://marcocuturi.net/) and [Rémi Flamary](http://remi.flamary.com/) exchanged on the proper ways to evaluate the various methods that do not optimize the same objectives. A particular point was listing the different applications -- genomics, computer graphics, domain adaptation, ... -- and the different requirements they had on the result of the OT problem -- a good estimate of the cost, of the map, of the Monge map ... Based on these applications, the consensus was that various metrics should be implemented in the benchmark for problems from the different domains, to better highlight the benefits from each approach.

- **[Sparse regression](https://github.com/TheoGuyard/benchmark_l0pen_ols_bigm)**:[Théo Guyard](https://theoguyard.github.io/), [Hippolyte Labarrière](https://www.math.univ-toulouse.fr/~hlabarri/) and [Matthieu Kowalski](http://hebergement.u-psud.fr/mkowalski/) benchmarked the various methods to perform sparse optimization. In particular, they proposed a way to compare results from sparse regression using the $\ell_1$ and $\ell_0$ norms.

- The **[$\ell_2$-regularized Logistic Regression benchmark](https://github.com/benchopt/benchmark_logreg_l2)**: [Mathieu Blondel](https://mblondel.org) extended the existing benchmark, published in our [NeurIPS 2022 paper](https://arxiv.org/abs/2206.13424). He added new methods based on the [jaxopt](https://jaxopt.github.io/stable/) library, in particular a novel efficient implementation of L-BFGS.
  
- The **[Total Variation benchmark](https://github.com/benchopt/benchmark_tv_1d/)**: [Pierre-Antoine Comby](https://github.com/paquiteau) and [Samuel Vaiter](https://samuelvaiter.com/) compared various solvers to minimize TV-regularized optimization problems, in 1D or 2D. During the sprint, several algorithms to compute proximal operators were developed and integrated into the existing benchmark, which was published in our [NeurIPS 2022 paper](https://arxiv.org/abs/2206.13424).
  
- The **Convolutional Dictionary Learning benchmark**: [Cedric Allain](https://fr.linkedin.com/in/c%C3%A9dricallain) compared different algorithms to learn dictionaries on large signals.
  
- The **Image Classification benchmarks for [ImageNet classification in PyTorch](https://github.com/agonon/benchmark_imagenet) and [ResNet optimization in jax](https://github.com/vroulet/benchmark_dl_jax)**: image classification tasks have always been used as benchmarks to develop novel optimization methods for deep learning. [Antoine Gonon](https://agonon.github.io/), [Leon Zheng](https://leonzheng2.github.io/) and [Vincent Roulet](https://vroulet.github.io/) strived to provide reproducible baselines for such tasks. The benchmark on ResNet optimization with `jax` aims to extend our previous **[cross-framework  benchmarks on ResNet for image classication](https://github.com/benchopt/benchmark_resnet_classif)**, which compared `pytorch` and `tensorflow` on various datasets, while the ImageNet benchmark aims to provide a reproducible and extendable implementation to compare different optimizers and architectures on ImageNet, in `PyTorch` with a single or multiple GPU(s).
  
- The **Domain Adaptation benchmark**: [Théo Gnassanou](https://scholar.google.com/citations?user=X_LZU3IAAAAJ&hl=fr), [Antoine Collas](https://www.antoinecollas.fr/) and [Antoine de Mathelin](https://scholar.google.com/citations?user=h79bffAAAAAJ&hl=fr) developed a  reproducible benchmark to evaluate the methods included in the currently under development package `skada`. With `benchopt`, they quickly were able to produce a benchmark with tens of methods and datasets. To improve this benchmark, we started to develop [a new feature]((https://github.com/benchopt/benchopt/pull/623)) to integrate cross-validation in the results.
  
- The **Federated Learning benchmark**: [Jean du Terrail](https://fr.linkedin.com/in/jean-du-terrail-30459a8b) leveraged the [FLamby datasets suite](https://github.com/owkin/FLamby) built by [Owkin](https://www.owkin.com/) and partners so that all FL strategies implemented in FLamby could be benchmarked on the 7 distributed healthcare datasets available in FLamby using benchopt. During this sprint, we focused on advancing the results presentation tools, which are necessary before the benchmark is released publicly.
  
  
The core developers team, composed of [Badr Moufad](https://github.com/Badr-MOUFAD), [Mathurin Massias](https://mathurinm.github.io/), [Benoit Malézieux](https://fr.linkedin.com/in/benoit-malezieux-203283148/en) and [Thomas Moreau](https://tommoral.github.io/), helped the participants with their questions and issues, and collected suggested improvements. We are already working on implementing these features, which will be shipped in the 1.5 release of benchopt!
