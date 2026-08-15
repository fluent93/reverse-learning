# From AI-Generated Output to Learner Ownership: A Reverse Learning Framework for Generative AI-Mediated Education

# Abstract

Generative artificial intelligence has intensified debates about academic integrity, authorship, assessment, and the future of learning. Much of the current educational response focuses on whether students used AI-generated text, often framing AI primarily as a threat to authentic learning. This article proposes a different question: under what conditions can AI-generated outputs become starting points for learning rather than substitutes for it? To address this question, the article introduces a Reverse Learning Framework for generative AI-mediated education. The framework describes a process in which learners begin with an AI-generated artifact and develop understanding through skepticism, verification, iterative prompting, contextual integration, human reconstruction, and explainable ownership. ==The framework's central explanatory mechanism is the fluency–validity gap: the discrepancy between the apparent completeness of AI-generated artifacts and their actual validity, relevance, and contextual fit. The article theorizes the motivational and self-regulatory conditions under which learners detect and act on this gap, articulates five propositions specifying how the framework's components relate, and develops explainable ownership as a three-layer construct comprising accountable authorship, epistemic ownership, and identity-level ownership.== Drawing on scholarship in generative AI in education, AI literacy, metacognition, ==self-regulated learning, motivation, cognitive offloading,== knowledge building, productive failure, assessment design, and reverse engineering, the framework reframes AI outputs as provisional learning objects that require human interrogation and reconstruction. It shifts the ethics of AI-assisted learning from a detection-based question—"Did the learner use AI?"—to an ownership-based question—"Can the learner explain, verify, contextualize, and defend the work?" The framework offers instructional designers, educators, and academic integrity policymakers practical strategies for designing AI-integrated assignments that preserve human epistemic responsibility. Reverse Learning is not the automation of learning; it is the humanization of AI-assisted learning.

Keywords: Reverse Learning; generative AI; AI literacy; learning design; human-AI interaction; metacognition; academic integrity; learner ownership; instructional design; epistemic responsibility

# 1. Introduction: The Problem of AI-Assisted Learning

Generative artificial intelligence has disrupted a long-standing assumption in education: that learners produce academic artifacts only after engaging with instruction, practice, and reflection. Today, learners may begin with a machine-generated essay, explanation, lesson plan, code sample, research summary, or presentation outline before they fully understand the underlying concepts. This shift has intensified concerns about academic integrity, authorship, assessment validity, and the erosion of authentic learning (==Bearman et al., 2023;== Cotton et al., 2024; Eaton, 2023; Kasneci et al., 2023).

These concerns are legitimate. If a learner submits an AI-generated artifact without understanding, verifying, or being able to explain it, little meaningful learning has occurred. In that case, generative AI functions as a tool for bypassing learning rather than supporting it. Yet the presence of an AI-generated artifact does not necessarily mean that learning has been bypassed. Under appropriate conditions, such artifacts may become starting points for critique, verification, dialogue, contextualization, and reconstruction, processes that align with research on metacognition, constructive engagement, and knowledge building (Chi & Wylie, 2014; Flavell, 1979; Scardamalia & Bereiter, 2006).

This distinction shifts the central educational question. The issue is not only whether learners use AI, but whether they develop ownership of AI-assisted work. A learner who uses AI to produce a polished answer but cannot explain its claims, evidence, assumptions, or limitations has delegated cognition without developing understanding. By contrast, a learner who uses AI-generated output as an object to question, verify, revise, and reconstruct may engage in a demanding form of learning involving critical thinking, metacognition, and epistemic responsibility (Eaton, 2023; Long & Magerko, 2020; Ng et al., 2021).

Emerging industry research on AI assistance and coding skill formation illustrates this distinction. Anthropic's coding-skills study reported that participants who used AI assistance scored 17% lower on a subsequent no-AI comprehension quiz than participants who coded by hand. However, the study also emphasized that lower performance was not caused by AI use alone; outcomes varied depending on how learners engaged with AI (Anthropic, 2026a). Although this evidence should be interpreted cautiously because it comes from an industry research context, it motivates the need for frameworks that distinguish passive delegation from inquiry-oriented AI use. ==This concern is consistent with peer-reviewed research on cognitive offloading, which shows that delegating cognitive work to external tools can reduce the engagement needed for durable learning, particularly when delegation becomes habitual (Gerlich, 2025; Risko & Gilbert, 2016).==

This article introduces a Reverse Learning Framework as a conceptual and practical model for designing such inquiry-oriented AI use. The framework proposes that learning in AI-rich environments may increasingly begin with a generated artifact and move backward into understanding. Rather than moving only from instruction to understanding to artifact production, learners may begin with an AI-generated artifact and then develop understanding through skepticism, verification, iterative prompting, contextual integration, human reconstruction, and explainable ownership.

The purpose of this article is not to argue that AI should replace teachers, experts, or learner effort. Nor does it suggest that all AI-assisted work is educationally valuable. Instead, it offers a framework for distinguishing educationally meaningful AI-assisted learning from superficial AI-assisted production. For educators and instructional designers, the practical challenge is to design assignments in which AI use leaves evidence of learner thinking rather than concealing its absence. The key question is not "Did the learner use AI?" but "Can the learner explain, verify, contextualize, and defend the work?"

# 2. Conceptual Positioning: What Kind of Article Is This?

This article is a conceptual framework paper. It does not report original empirical findings. Rather, it synthesizes scholarship on generative AI in education, AI literacy, metacognition, ==self-regulated learning, motivation,== knowledge construction, academic integrity, productive failure, and reverse engineering to develop a model of AI-mediated learning. Following Jaakkola's (2020) typology of conceptual articles, the paper is positioned as a model-oriented conceptual contribution: it identifies key constructs, proposes relationships among those constructs, and explains how the resulting model can guide educational design and future research. ==To meet this standard, the article specifies not only the framework's components but also the mechanisms and relationships that connect them, formalized as five propositions in Section 5.==

The conceptual work in this article follows three design moves. First, it identifies a practical and theoretical problem: generative AI allows learners to obtain polished artifacts before they have developed corresponding understanding. Second, it synthesizes adjacent bodies of scholarship to explain why this problem matters for learning design, including AI literacy, metacognition, ==motivation and self-regulation,== knowledge building, academic integrity, assessment design, and reverse engineering. Third, it proposes a ==conceptual model== that links learner actions, observable evidence, and assessment possibilities, ==and that explains why and under what conditions those actions unfold.==

The article contributes to learning design in ==four== ways. First, it reframes AI-generated outputs as provisional learning objects rather than final answers. Second, it conceptualizes iterative prompting as a metacognitive dialogue rather than merely a production technique. Third, it connects AI ethics and assessment design by shifting the focus from detection-based control to ownership-based accountability. ==Fourth, it identifies the fluency–validity gap as the explanatory mechanism that distinguishes Reverse Learning from adjacent frameworks and theorizes the conditions under which learners detect and act on that gap.==

This framing is particularly relevant for instructional designers, educators, faculty developers, corporate learning professionals, and academic integrity policymakers. In many educational settings, current responses to generative AI focus on prohibition, detection, or disclosure ==(UNESCO, 2023)==. Although these responses may be necessary in some contexts, they are insufficient as learning design strategies. Learners also need structured processes that help them use AI critically and responsibly. The Reverse Learning Framework is proposed as one such process. Because this manuscript is designed for readers concerned with the practical application of educational technology, it emphasizes not only conceptual definition but also assignment design, observable learning evidence, and assessment strategies.

# 3. Theoretical Background

## 3.1 Generative AI and the Challenge of Learner Ownership

Generative AI systems can produce fluent, structured, and contextually responsive texts, explanations, code, and designs. In educational settings, this creates both opportunity and risk. On one hand, AI can support brainstorming, tutoring, feedback, language refinement, simulation, and personalized assistance. Kasneci et al. (2023), for example, describe large language models as potentially useful for educational support while also emphasizing risks related to accuracy, bias, transparency, and overreliance. Mollick and Mollick (2023) similarly describe multiple educational roles for AI, including tutor, coach, mentor, teammate, tool, simulator, and student. Lodge et al. (2023) argue that generative AI should not be understood simply by analogy to earlier educational technologies such as calculators; rather, learner-AI relationships require more nuanced conceptualization. On the other hand, AI can make it easier for learners to produce artifacts without developing corresponding understanding.

The problem is not simply that AI can generate outputs. Educational technologies have long mediated learning artifacts. Calculators, search engines, writing tools, and learning management systems have all changed what learners can produce. However, generative AI differs from many earlier tools because it can participate in the production of language, reasoning, explanation, and design in ways that appear conversational and agent-like (Lodge et al., 2023; Mollick & Mollick, 2023). The distinctive challenge of generative AI is that it can produce artifacts that appear complete, coherent, and authoritative. This fluency may obscure the learner's lack of understanding and complicate assessment of authorship, integrity, and conceptual mastery (Cotton et al., 2024; Eaton, 2023). A learner may possess a finished-looking product without possessing the conceptual, evidentiary, or rhetorical control needed to defend it.

This article uses the term learner ownership to describe the learner's intellectual responsibility for an artifact. Ownership does not mean that no tools were used. Rather, it means the learner can explain the artifact's claims, justify its evidence, identify its limitations, adapt it to context, and revise it in response to critique. In AI-assisted work, ownership is not automatic. It must be designed for through assessment practices that make learner reasoning and responsibility visible (Perkins et al., 2024; WAME, 2023).

Emerging industry evidence from Anthropic's coding-skills study illustrates why this distinction matters. In that study, participants who used AI assistance scored lower on a subsequent no-AI comprehension quiz than participants who coded by hand, even though AI assistance helped them complete the original task. The study also reported that outcomes depended on how learners used AI (Anthropic, 2026a). This finding is important for Reverse Learning because it suggests that AI assistance should not be evaluated only by speed or output quality. A learner may complete a task while failing to develop transferable understanding. The educational design challenge is to prevent passive delegation and promote active reconstruction.

## 3.2 AI Literacy and Critical Verification

AI literacy provides one foundation for Reverse Learning. Long and Magerko (2020) define AI literacy as a set of competencies that enable individuals to critically evaluate, communicate with, and collaborate with AI technologies. Ng et al. (2021) similarly conceptualize AI literacy as involving knowledge and understanding, use and application, evaluation and creation, and ethical awareness. These dimensions are directly relevant to Reverse Learning because learners must not only use AI but also evaluate its outputs and understand their own responsibilities in relation to those outputs.

In the Reverse Learning Framework, AI literacy is not treated as a separate preliminary skill. It is embedded in the learning process. When learners question an AI-generated output, identify unsupported claims, check sources, test generated code, or ask AI to explain its assumptions, they are practicing AI literacy. Verification becomes a learning mechanism rather than merely a compliance requirement.

This distinction matters because many learners may equate AI fluency with the ability to obtain fast, polished responses. However, AI fluency should also involve scrutiny, calibration, and judgment. Anthropic's AI Fluency Index, for example, frames effective human-AI collaboration as a set of observable behaviors rather than mere tool adoption and emphasizes iteration and refinement as central features of fluent AI use (Anthropic, 2026b). A key implication for Reverse Learning is that AI-generated artifacts should trigger more questioning, not less. ==This orientation also aligns with broader scholarship on human-AI collaboration in learning, which emphasizes that productive collaboration requires humans and AI systems to contribute complementary strengths rather than humans deferring wholesale to machine output (Järvelä et al., 2023).==

Critical verification also responds to a central problem in AI-assisted learning: generated content can sound credible even when it is inaccurate, incomplete, or weakly supported. Therefore, verification should be treated as a designed learning activity. Learners can be asked to identify claims requiring evidence, locate authoritative sources, compare AI-generated explanations with course readings, and revise the artifact based on verified information.

## 3.3 Metacognition, Self-Explanation, and Cognitive Engagement

Reverse Learning is also grounded in metacognition. Flavell (1979) describes metacognition as knowledge and regulation of one's own cognitive processes. In AI-mediated learning, this includes asking: What do I understand? What did AI generate that I cannot yet explain? Which parts of this output do I trust, and why? What must I verify? What would I need to know in order to defend this claim?

Iterative prompting can support metacognition when learners use AI not only to produce answers but also to test and refine their understanding. For example, a learner may ask AI to identify assumptions, generate counterarguments, compare theoretical perspectives, quiz the learner, or point out gaps in reasoning. In this use, prompting becomes a form of metacognitive dialogue. Prompting is not merely a production technique; it becomes a reflective practice through which learners monitor and regulate understanding.

The ICAP framework is useful for understanding why this matters. Chi and Wylie (2014) distinguish passive, active, constructive, and interactive forms of engagement. A learner who merely reads and submits AI-generated text remains largely passive. A learner who edits surface features may be active. A learner who reorganizes, explains, and reconstructs ideas becomes constructive. A learner who engages in iterative dialogue to test and revise understanding becomes interactive. Reverse Learning is designed to move learners from passive acceptance toward constructive and interactive engagement.

Self-explanation is also relevant. When learners explain why a claim is valid, why evidence supports it, or why a revision was necessary, they make their understanding available for inspection. In Reverse Learning, self-explanation can be embedded in oral defenses, ownership statements, revision rationales, and prompting reflections.

==## 3.4 Learner Agency, Motivation, and the Activation of Skepticism==

==The stages described in this framework do not unfold automatically. A framework that sequences learner behaviors—skepticism, verification, iterative prompting—must also explain the conditions under which learners actually engage in those behaviors. Many students approach generative AI primarily as an efficiency tool: research on cognitive offloading shows that people routinely delegate cognitive work to external systems to reduce effort, and that frequent, habitual offloading to AI tools is associated with reduced critical engagement (Gerlich, 2025; Risko & Gilbert, 2016). An account of Reverse Learning that presupposes a critically motivated learner would therefore describe an idealized process rather than a realistic one. This section theorizes learner agency within the framework using two established motivational perspectives: self-regulated learning and expectancy-value theory.==

==Self-regulated learning (SRL) theory describes learning as a cyclical process of forethought, performance, and self-reflection, in which learners set goals, monitor their activity, and evaluate outcomes against standards (Zimmerman, 2000, 2002). Reverse Learning can be understood as a domain-specific instantiation of this cycle in AI-mediated contexts. In the forethought phase, the learner's goal orientation determines whether an AI-generated artifact is framed as a finished product to submit or as a provisional object to interrogate. In the performance phase, skepticism and verification function as self-monitoring directed at an external artifact rather than at one's own memory: the learner compares the artifact's claims against internal standards and external sources. In the self-reflection phase, reconstruction and ownership judgments correspond to self-evaluation, in which learners judge whether they could explain and defend the artifact without assistance. From an SRL perspective, the failure modes identified in Section 5 are failures of regulation: a learner who submits an unexamined AI output has bypassed monitoring entirely, not merely skipped a step in a workflow.==

==Expectancy-value theory explains when learners are likely to invest this regulatory effort (Eccles & Wigfield, 2020). Engagement in skepticism and verification carries a real cost in time and effort, which is precisely what efficiency-oriented AI use seeks to minimize. Learners will sustain the Reverse Learning process when they expect to succeed at verification and reconstruction, when they value the resulting understanding, and when the perceived cost of engagement does not outweigh these benefits. Empirical work applying expectancy-value theory to generative AI adoption supports this analysis: students' perceived value of generative AI strongly predicts their intention to use it, while perceived costs weigh against particular forms of use (Chan & Zhou, 2023). The design implication is direct. If assessment rewards only the polish of the final artifact, the rational strategy is passive delegation, because verification adds cost without adding perceived value. If assessment makes understanding visible and consequential—through oral defense, revision rationales, or transfer tasks—the value calculus shifts in favor of critical engagement.==

==This analysis clarifies what triggers a learner to question an AI-generated artifact rather than accept it. Three classes of conditions matter. Dispositional conditions include a learner's need for cognition (Cacioppo & Petty, 1982), epistemic curiosity, and calibration of trust in AI systems; learners who enjoy effortful thinking or who have previously encountered AI errors are more likely to initiate skepticism spontaneously. Contextual conditions include classroom norms that treat AI output as an object of critique, instructor modeling of verification, and—most powerfully—assessment designs that announce in advance that learners must explain and defend their work without AI assistance. Task-level conditions include the personal relevance of the task, the verifiability of its claims, and its stakes; learners are more likely to verify claims they will be held accountable for and that connect to contexts they care about.==

==The Reverse Learning Framework therefore does not assume that skepticism arises naturally. It treats the activation of skepticism as a design problem. The pedagogical structures described in Section 8—critique assignments, verification logs, oral defenses, ownership statements—are not merely assessment instruments; they are the contextual conditions that make critical engagement the expected and rewarded pathway. In this respect, the framework aligns with hybrid human-AI regulation research, which argues that productive human-AI learning requires deliberately designed triggers and supports rather than assumptions of spontaneous learner initiative (Järvelä et al., 2023).==

## 3.5 Knowledge Building and Human Reconstruction

Reverse Learning also draws on knowledge building. Scardamalia and Bereiter (2006) describe knowledge building as the creation and improvement of conceptual artifacts. From this perspective, ideas are not simply received; they are developed, tested, improved, and shared. This is highly relevant to AI-generated work. An AI output can be treated as an improvable conceptual artifact rather than a completed answer. ==Human reconstruction is therefore central to Reverse Learning.== Learners must do more than copyedit AI-generated text. They must reorganize arguments, remove weak claims, add verified evidence, contextualize examples, and articulate reasoning in their own voice. Reconstruction is the point at which AI-assisted material becomes learner-owned knowledge.

This process is also important for professional learning. In workplace contexts, generalized AI output often lacks organizational, cultural, technical, and strategic context. A corporate learning professional, software engineer, instructional designer, or graduate student must adapt AI-generated material to real constraints, audiences, and goals. Such contextual adaptation is not a minor editing task; it is a core learning act.

## 3.6 Productive Failure and Learning from Imperfect Outputs

The Reverse Learning Framework does not assume that AI outputs are always accurate or useful. In fact, the imperfection of AI outputs can become educationally productive when learners are required to identify, verify, and reconstruct them. This idea is related to productive failure, which suggests that initial struggle or incomplete problem solving can prepare learners for deeper understanding (Kapur, 2008, 2016).

However, Reverse Learning differs from productive failure in an important way. In productive failure, learners typically struggle with a problem before receiving instruction or a canonical solution. In Reverse Learning, learners may begin with a seemingly complete solution generated by AI. The productive struggle occurs when learners discover that the output's fluency does not guarantee validity, relevance, or ownership. The failure is not necessarily in the learner's initial attempt, but in the artifact's incompleteness and the learner's potential overtrust. ==This distinction is particularly important in AI-assisted learning because AI-generated text often appears polished enough to preempt productive struggle altogether. Reverse Learning reintroduces productive struggle by requiring skepticism, verification, and reconstruction.==

## 3.7 Reverse Engineering as a Conceptual Metaphor

The term "Reverse Learning" is inspired by reverse engineering. In software and engineering contexts, reverse engineering involves analyzing an existing system or artifact to understand its structure, function, assumptions, and design logic. Chikofsky and Cross's (1990) taxonomy of reverse engineering and design recovery provides a useful conceptual foundation for this metaphor.

Reverse Learning applies a similar logic to AI-mediated education. Learners begin with an existing artifact—an AI-generated response, draft, explanation, or design. They then work backward to uncover the claims, evidence, assumptions, conceptual structure, and reasoning embedded in that artifact. The goal is not merely to inspect the artifact but to reconstruct it in a way that reflects human understanding and responsibility.

The metaphor is not perfect. Learning is not engineering, and AI-generated text is not a mechanical system. Nevertheless, the reverse engineering metaphor captures a key shift: learners may increasingly encounter outputs before they understand the processes that generated or justify those outputs. Reverse Learning names the educational work required to move from output back to understanding.

==## 3.8 An Integrated Account: The Fluency–Validity Gap and the Transfer of Epistemic Responsibility==

==The theoretical foundations reviewed above are not merely a list of adjacent literatures; each explains a different part of the Reverse Learning process, and their integration reveals what none of them explains alone. AI literacy research supplies the evaluative competencies that skepticism and verification require (Long & Magerko, 2020; Ng et al., 2021). Metacognition and the ICAP framework explain why the quality of engagement—passive, active, constructive, or interactive—determines whether interaction with an artifact produces understanding (Chi & Wylie, 2014; Flavell, 1979). Self-regulated learning and expectancy-value theory explain when learners will invest the effort that critical engagement demands (Eccles & Wigfield, 2020; Zimmerman, 2002). Knowledge building explains how artifacts function as improvable objects rather than terminal products (Scardamalia & Bereiter, 2006). Productive failure explains why imperfect artifacts can be more educative than perfect ones (Kapur, 2008). Reverse engineering supplies the structural logic of working backward from artifact to underlying rationale (Chikofsky & Cross, 1990).==

==What none of these frameworks explains, however, is the learning situation that generative AI has made pervasive: a learner holds a complete-appearing, fluent artifact that they did not produce and do not yet understand. AI literacy describes competencies but not a learning process that begins from a generated artifact. Metacognitive and engagement theories presuppose content whose difficulty is apparent; they do not address artifacts whose fluency actively conceals their defects. Productive failure assumes the learner struggles before encountering a canonical solution, whereas here a pseudo-canonical solution arrives first. Knowledge building assumes a community improving its own artifacts, not an individual confronting a machine-generated one. Each theory, in short, assumes either that the learner starts without an artifact or that the artifact's imperfections are visible. Generative AI violates both assumptions simultaneously.==

==The Reverse Learning Framework introduces an explanatory mechanism for this situation: the fluency–validity gap. AI-generated artifacts systematically exhibit a discrepancy between their apparent quality—coherence, confidence, completeness—and their actual validity, evidential grounding, and contextual fit. This gap has two properties that make it educationally consequential. First, it is invisible by default: fluency masks the very defects that would otherwise trigger scrutiny, which is why passive acceptance is the path of least resistance. Second, it is discoverable by design: when learners are required to flag uncertain claims, verify evidence, and adapt content to context, the gap becomes visible, and its discovery functions as the moment of productive struggle that initiates genuine learning. The framework's stages describe the progressive discovery and resolution of this gap. Skepticism postulates the gap's existence; verification locates it; iterative prompting and contextual integration probe its boundaries; reconstruction closes it; and explainable ownership demonstrates that it has been closed.==

==Resolving the fluency–validity gap accomplishes what this article calls the transfer of epistemic responsibility. At the start of the process, the epistemic warrant for the artifact's claims resides—illegitimately—in the machine's fluency. Through verification and reconstruction, warrant is progressively re-grounded in sources, evidence, and reasoning that the learner can access, evaluate, and articulate. Explainable ownership names the end state of this transfer: the learner, not the machine, becomes the accountable epistemic agent for the final artifact. This mechanism is what distinguishes Reverse Learning from a generic exhortation to think critically about AI. It specifies what learners must discover (the gap), why the discovery is educative (it converts concealed defects into objects of productive struggle), and what the process must produce (re-grounded, learner-held warrant).==

==The framework therefore uniquely captures three phenomena that adjacent frameworks do not. First, artifact-first learning: a learning trajectory that begins after a complete-appearing answer exists. Second, pseudo-competence: the possession of a polished artifact without the understanding needed to defend it, which detection-oriented integrity approaches cannot distinguish from genuine competence. Third, ownership without sole authorship: the condition in which a learner is the accountable epistemic agent for work that a machine helped produce. These phenomena define the empirical territory on which the framework's claims can be tested, as elaborated in the research agenda in Section 10.==

# 4. Defining Reverse Learning

Reverse Learning is an AI-mediated learning process in which learners begin with an AI-generated artifact and develop understanding by critically verifying, deconstructing, revising, contextualizing, and reconstructing that artifact until they can explain and defend the final work as their own.

==In traditional learning, the sequence is often represented as instruction, then understanding, then practice, then artifact production. In Reverse Learning, the sequence is partially reversed: the learner begins with an AI-generated artifact and moves through questioning, verification, and reconstruction toward understanding and ownership. The word "partially" is important. Reverse Learning does not claim that all learning is reversed or that instruction is no longer needed. Rather, it describes a specific pattern that has become more visible in generative AI environments: learners may begin with a generated artifact and then work backward into understanding. The AI output is not the final answer; it is the starting point.==

==Reverse Learning becomes educationally valuable only when learners actively interrogate and reconstruct AI-generated outputs. If learners simply accept AI outputs, the process becomes passive delegation. If learners question, verify, contextualize, and rebuild those outputs, the process can support learning. As theorized in Section 3.8, what separates these two trajectories is whether the fluency–validity gap is discovered and resolved or remains concealed beneath the artifact's polish.==

# 5. The Reverse Learning Framework

The Reverse Learning Framework consists of seven ==components==: AI-Generated Artifact, Learner Skepticism, Verification, Iterative Prompting, Contextual Integration, Human Reconstruction, and Explainable Ownership. ==These components are presented sequentially for clarity, but the framework is not a strict linear pipeline. This section first specifies how the components relate to one another, then describes each component with its key learner actions, observable evidence, and characteristic failure mode.==

[FIGURE 1 HERE]

Figure 1. The Reverse Learning Framework

==Figure 1 caption. The Reverse Learning Framework represents an artifact-first path to understanding in AI-mediated education. An AI-generated artifact enters the process through learner skepticism, which functions as an epistemic gateway: if skepticism is not activated, the process terminates in passive delegation (dashed path). Verification and iterative prompting form a mutually reinforcing inquiry loop in which external checking disciplines dialogue with the AI and dialogue surfaces new claims to check. Contextual integration and human reconstruction convert verified content into learner-owned work, with feedback paths returning to the inquiry loop when integration or reconstruction exposes new gaps. Explainable ownership is the exit state, reached when the learner can explain, defend, and revise the artifact without AI assistance.==

==## 5.1 Relationships Among Components==

==A conceptual framework must specify not only its constructs but also how and why they relate (Jaakkola, 2020). Five propositions formalize these relationships. They are stated as testable claims to guide both implementation and the research agenda in Section 10.==

==Proposition 1 (Gateway). Learner skepticism is the necessary entry condition for all subsequent components. The AI-generated artifact and learner skepticism jointly initiate the process: the artifact supplies the object of inquiry, and skepticism converts it from an answer into a question. If skepticism is not activated—whether for dispositional, contextual, or task-level reasons (Section 3.4)—no amount of available scaffolding produces verification or reconstruction, and the process collapses into passive delegation. This is why the framework treats the activation of skepticism as a design responsibility rather than a learner trait.==

==Proposition 2 (Inquiry loop). Verification and iterative prompting are mutually constitutive and can occur simultaneously; neither is a strict prerequisite for the other. A learner may verify a claim externally and return to the AI to probe an inconsistency, or a prompting exchange may surface a new claim that requires external verification. The relationship is nonetheless asymmetric in one respect: because a generative model cannot serve as the warrant for its own claims, external verification must ultimately discipline the prompting dialogue. Prompting without verification degrades into rhetorical polishing; verification without prompting forfeits the metacognitive benefits of dialogue.==

==Proposition 3 (Conversion). Contextual integration and human reconstruction convert verified content into learner-owned knowledge, and this conversion routinely sends learners backward. Adapting an artifact to a specific audience, institution, or problem context frequently exposes claims that were never checked and assumptions that do not transfer, triggering regression to the inquiry loop. Regression is therefore not a deviation from the process but evidence that it is working: each return pass narrows the fluency–validity gap further.==

==Proposition 4 (Exit criterion). Explainable ownership is a state to be demonstrated, not a stage to be completed. The process ends when the learner can explain the artifact's claims, justify its evidence, acknowledge its limitations, and revise it under critique without AI assistance—regardless of how many iterations were required. Conversely, completing every activity in sequence without meeting this criterion does not constitute Reverse Learning.==

==Proposition 5 (Compression and its limits). The process can be legitimately compressed but not selectively skipped. For low-stakes tasks or content within the learner's expertise, skepticism, verification, and reconstruction may be rapid and partially internalized. However, two omissions produce characteristic failure modes regardless of compression: omitting verification leaves machine fluency as the artifact's only warrant (uncritical delegation), and omitting reconstruction leaves the learner editing prose they cannot defend (surface editing). Compression is a function of expertise and stakes; omission is a failure of the process.==

==Together, these propositions describe a mechanism rather than a checklist: skepticism opens the fluency–validity gap to inspection (P1), the inquiry loop locates and probes it (P2), conversion closes it in context (P3), ownership certifies its closure (P4), and expertise governs how quickly the cycle runs (P5).==

==## 5.2 The Seven Components==

### Stage 1: AI-Generated Artifact

The process begins when a learner uses generative AI to produce an initial artifact. This artifact may be an essay draft, literature summary, lesson plan, code example, project proposal, presentation outline, or conceptual explanation. At this stage, the artifact should not be treated as complete or authoritative. It is a provisional object for investigation. The key learner action is to generate or obtain an initial AI output and explicitly label it as provisional. Observable evidence may include the initial AI output, the original prompt, and a note identifying the output as a draft or object of analysis. The failure mode occurs when the learner treats the AI output as complete and submits it without interrogation. ==Because the quality of this initial artifact depends substantially on the quality of the prompts that produced it, prompt literacy functions as a prerequisite competency for this stage, as discussed in Section 6 (Knoth et al., 2024).==

### Stage 2: Learner Skepticism

Learner skepticism is the adoption of a critical stance toward the AI-generated artifact. This stage is essential because AI outputs often appear fluent, confident, and well-organized even when they contain errors, unsupported claims, missing context, or weak reasoning. Learner skepticism does not mean rejecting AI. It means refusing to treat AI fluency as evidence of truth. This stage connects to critical thinking, epistemic cognition, and AI literacy. The learner asks: What might be wrong here? Which claims need evidence? What assumptions are hidden? What perspectives are missing? What does not fit my context?

Observable evidence may include annotations, flagged claims, margin comments, or a list of questions generated from the AI output. The failure mode occurs when the learner trusts AI fluency as authority and does not notice unsupported or inaccurate claims. A useful design principle is to require learners to mark uncertainty before revising. For example, an instructor might ask students to highlight all claims in an AI-generated output that require verification, all claims that seem plausible but unsupported, and all claims that do not fit the learner's context. This makes skepticism observable rather than merely attitudinal.

### Stage 3: Verification

Verification is the process of checking AI-generated claims, examples, calculations, citations, or code against credible sources, course materials, data, domain knowledge, or expert feedback. In Reverse Learning, verification is not an optional academic integrity step. It is a core learning mechanism. The key learner action is to test the artifact's validity. This may involve checking citations, comparing claims with peer-reviewed literature, validating calculations, running code, consulting documentation, or asking an instructor or expert for clarification. Observable evidence may include a verification log, source comparison table, corrected citations, fact-checking notes, or code testing records. The failure mode occurs when hallucinated references, weak evidence, inaccurate explanations, or invalid assumptions remain in the final artifact.

### Stage 4: Iterative Prompting

Iterative prompting is repeated dialogue with AI to clarify, challenge, compare, revise, and deepen understanding. In Reverse Learning, prompting is not merely a technique for producing better outputs. It is a learning process. The learner may ask AI to identify assumptions, generate counterarguments, explain reasoning, compare theories, simplify a concept, quiz the learner, or critique a draft. Through this process, the learner becomes more aware of the structure of the problem and the quality of possible responses.

Observable evidence may include prompt histories, revised prompts, reflection notes, and explanations of how prompting changed the learner's understanding. The failure mode occurs when prompting is used only to make prose sound more polished rather than to improve understanding. ==As Proposition 2 specifies, this stage operates in a loop with verification: external checking supplies the standards against which the learner evaluates what the AI says next.==

### Stage 5: Contextual Integration

Contextual integration occurs when the learner connects AI-generated content with personal, professional, cultural, institutional, and situational context. AI systems may possess broad general knowledge, but they do not automatically understand the learner's lived experience, workplace environment, institutional constraints, professional judgment, or cultural background. A generic AI-generated explanation may be technically correct but contextually inadequate. The learner must adapt the output to actual audiences, constraints, goals, and values.

Observable evidence may include workplace-specific examples, culturally relevant explanations, references to institutional constraints, personal reflection, or adaptation for a specific learner population. The failure mode occurs when the final artifact remains generic, polished, and detached from the learner's actual learning environment.

### Stage 6: Human Reconstruction

Human reconstruction is the process of rewriting, reorganizing, and rebuilding the artifact in the learner's own voice and reasoning structure. This is more than editing. It is the moment when AI-assisted material becomes personally understood work. The learner removes unsupported claims, adds verified evidence, revises examples, changes structure, clarifies definitions, and articulates the logic of the final artifact. Reconstruction requires the learner to make decisions and take responsibility for those decisions.

Observable evidence may include revision histories, before-and-after comparisons, rationale statements for major changes, and final drafts that differ conceptually from the initial AI output. The failure mode occurs when the learner performs only surface-level editing without changing reasoning, evidence, or conceptual structure.

### Stage 7: Explainable Ownership

Explainable ownership is the ability to explain, defend, and revise the final artifact without relying on AI. It is the culminating ==state== of Reverse Learning. A learner demonstrates explainable ownership when they can explain the main argument, justify the evidence, identify limitations, respond to critique, and revise the work in light of feedback. Ownership does not mean that AI was not used. It means that the learner has taken intellectual responsibility for the final artifact.

==Because explainable ownership is the framework's central outcome construct, it requires more precise conceptualization than the term "ownership" alone provides. Ownership of AI-assisted work can be distinguished into three layers that carry different theoretical commitments and different assessment implications. The first layer is accountable authorship: the learner's claim that they directed, curated, and take public responsibility for the artifact's production. This layer draws on scholarly authorship norms, which hold that responsibility—not unaided origination—is the defining criterion of authorship in AI-assisted work (Eaton, 2023; WAME, 2023). The second layer is epistemic ownership: the learner's claim to understand the artifact—to know why its claims are true, how its evidence supports them, and where its limits lie. This layer draws on research in epistemic cognition, which concerns how people evaluate the sources and justification of knowledge (Chinn et al., 2011). The third layer is identity-level ownership: the learner's sense that the artifact reflects their own thinking, voice, and commitments. This layer draws on psychological ownership research, which describes how objects become experienced as part of the extended self through control, intimate knowledge, and self-investment (Pierce et al., 2003).==

==These layers are related but dissociable, and the framework does not weight them equally. Epistemic ownership is the non-negotiable core of Reverse Learning in all task types: without it, neither accountable authorship nor identity-level ownership has educational substance, because a learner cannot take meaningful responsibility for—or identify with—claims they cannot explain. Accountable authorship is likewise required whenever work is submitted or published, but the framework deliberately redefines it: in AI-mediated contexts, authorship means accountable curation and reconstruction rather than sole origination. Identity-level ownership, by contrast, varies legitimately with task type. It is central in reflective, argumentative, and creative work, where the artifact expresses the learner's positions and voice, but it may be peripheral in technical or procedural tasks, where a learner can fully understand and stand behind a verified solution without experiencing it as self-expressive. Notably, Pierce et al. (2003) identify intimate knowing and invested effort as primary routes to psychological ownership, which suggests that the verification and reconstruction stages are themselves the mechanism by which identity-level ownership develops when it develops at all.==

==Table 1 summarizes the three layers and maps each onto the assessment evidence described in Section 8: ownership statements primarily document accountable authorship, oral defenses and transfer tasks primarily test epistemic ownership, and reflective memos primarily surface identity-level ownership.==

==Table 1. Three Layers of Explainable Ownership==

==[TABLE]==
==Layer | Core claim | Theoretical grounding | Primary assessment evidence==
==Accountable authorship | "I directed this work and take responsibility for it." | Authorship and integrity norms (Eaton, 2023; WAME, 2023) | Ownership statement; AI use disclosure==
==Epistemic ownership | "I understand this work and can justify its claims." | Epistemic cognition (Chinn et al., 2011) | Oral defense; instructor questioning; transfer task==
==Identity-level ownership | "This work reflects my own thinking and voice." | Psychological ownership (Pierce et al., 2003) | Reflective memo; revision rationale==
==[/TABLE]==

Explainable ownership also provides an assessment response to generative AI. Instead of relying only on AI detection tools, educators can design tasks that require learners to demonstrate understanding in ways that are difficult to outsource completely: explaining decisions, defending evidence, responding to follow-up questions, revising under critique, and transferring ideas to a new case. ==The failure mode occurs when the learner cannot explain submitted work, justify its claims, or revise it under questioning—that is, when accountable authorship is claimed but epistemic ownership is absent.==

Table ==2==. Reverse Learning Prompts

[TABLE]
Reverse Learning Stage | Prompt Type | Example Prompt
Skepticism | Assumption check | What assumptions does this response make?
Skepticism | Weakness detection | Which parts of this draft are weak, vague, or unsupported?
Verification | Evidence check | Which claims in this response require external evidence?
Verification | Source validation | Identify claims that should be verified with peer-reviewed or authoritative sources.
Iterative Prompting | Counterargument | What are the strongest objections to this argument?
Iterative Prompting | Conceptual comparison | Compare this explanation with constructivist learning theory.
Contextual Integration | Personalization | Rewrite this for a learner with professional experience in software engineering and corporate training.
Human Reconstruction | Structure revision | Suggest a stronger structure, but do not rewrite the full draft for me.
Explainable Ownership | Oral defense | Ask me five questions to test whether I truly understand this argument.
Explainable Ownership | Limitation awareness | What limitations or uncertainties should I be prepared to explain?
[/TABLE]

==# 6. Learner Readiness, Prerequisites, and Scaffolding==

==The Reverse Learning process makes real demands on learners. Identifying inaccuracies presupposes enough disciplinary knowledge to recognize what a plausible error looks like; verifying claims presupposes source evaluation skills; reconstructing an artifact presupposes the writing and reasoning capacity to rebuild it. These prerequisites are not distributed equally, and a framework that ignored this would risk functioning best for the learners who need it least. This section specifies the competencies the framework presupposes, how implementation should differ for novice and expert learners, and the scaffolds that make the process accessible.==

==Three prerequisite competencies matter most. The first is baseline domain knowledge. Skepticism and verification are knowledge-dependent: a learner cannot flag an unsupported claim in a domain whose claims they cannot parse. For novices, this does not make Reverse Learning inapplicable, but it changes what verification means—novices verify against supplied course materials, curated source lists, and instructor feedback rather than against internalized expertise. The second is source evaluation skill: the ability to distinguish authoritative from unreliable sources, which verification presupposes and strengthens. The third is prompt literacy. The quality of the initial AI-generated artifact and the productivity of iterative prompting both depend heavily on the quality of the learner's prompts; empirical work shows that prompt engineering skill predicts the quality of AI output and is itself shaped by AI literacy (Knoth et al., 2024). A learner with weak prompt literacy begins the process with a weaker artifact and extracts less from the dialogue stages. Reverse Learning both requires and develops prompt literacy: initial implementations should supply prompt templates (such as those in Table 2), while later implementations can require learners to design and justify their own prompts.==

==Novice and expert learners should therefore encounter the framework differently. Research on the expertise reversal effect shows that instructional supports that benefit novices can burden more experienced learners, and vice versa (Kalyuga, 2007). For novices, the process should be heavily externalized: claim-flagging templates that specify what kinds of statements require checking, verification logs with pre-identified source lists, sentence starters for revision rationales, and instructor modeling of the full cycle on a shared example. For advanced learners, these structures can be progressively removed so that skepticism, verification, and reconstruction operate as internalized habits, consistent with Proposition 5's account of legitimate compression. A gradual release model—instructor demonstration, scaffolded practice, independent application—maps naturally onto this progression.==

==These considerations carry direct equity implications. Learners with stronger prior knowledge, better developed metacognitive skills, and more prior AI experience are better positioned to execute every stage of the process. If Reverse Learning is assigned without scaffolds, it may therefore amplify existing advantages rather than reduce them. The framework's position is that these supports are constitutive of the framework, not optional additions: an implementation without scaffolds, source access, exemplars, and feedback opportunities is not a lean version of Reverse Learning but a defective one. Institutions adopting the framework should treat scaffold provision—including access to verification resources such as library databases—as a baseline implementation requirement, particularly in settings serving learners with uneven preparation.==

# 7. Distinguishing Reverse Learning from Related Concepts

Reverse Learning is related to several existing concepts, but it is not identical to them. The framework's novelty lies in its artifact-first sequence, its focus on AI-generated outputs, and its emphasis on explainable learner ownership. Table ==3== is intended to clarify conceptual boundaries. It addresses a likely reviewer question: whether Reverse Learning is merely a new name for flipped learning, backward design, productive failure, AI literacy, or general critical thinking. The comparison shows that Reverse Learning is not defined by a general reversal metaphor alone, but by the specific sequence in which learners begin with AI-generated artifacts and work toward understanding through verification and reconstruction.

Table ==3==. Reverse Learning and Related Concepts

[TABLE]
Concept | What is reversed or reorganized? | Primary actor | Key distinction
Flipped learning | Time/place of instruction and practice | Instructor / designer | Reorganizes instructional sequence; does not begin with AI-generated artifacts.
Backward design | Curriculum planning sequence | Instructional designer | Begins with outcomes and assessments; focuses on course design.
Reversal learning | Stimulus-response contingency | Organism / learner | Describes adaptation to changed contingencies in psychology/neuroscience.
Reverse learning in machine learning | Path from goal state to starting state | Algorithm | Describes computational learning strategies, not human learner ownership.
Productive failure | Learning through initial struggle | Learner | Values productive struggle but does not specifically address AI-generated outputs.
AI literacy | Competencies for understanding and using AI | Learner / educator | Provides broad competencies; does not specify an artifact-first reconstruction process.
AI as tutor/coach/student | Role assigned to AI | Learner and AI | Defines AI roles; does not specify an artifact-first reconstruction process.
Reverse Learning Framework | Artifact-first path to understanding | Human learner with AI | Begins with AI output and moves toward verification, reconstruction, and explainable ownership.
[/TABLE]

Flipped learning reverses the location and timing of content exposure and practice ==(Flipped Learning Network, 2014)==. Backward design reverses the sequence of curriculum planning by beginning with desired outcomes ==(Wiggins & McTighe, 2005)==. Reversal learning in psychology concerns adaptation when learned contingencies change. Reverse learning in machine learning may refer to computational approaches that work backward from target states. Reverse Learning, as proposed here, concerns human learning in AI-mediated environments.

This distinction is important because Reverse Learning is not simply "critical thinking plus AI." Critical thinking is necessary but not sufficient. Reverse Learning specifies a particular sequence and mechanism: learners begin with AI-generated artifacts, interrogate them through iterative human-AI dialogue, verify them against external sources, reconstruct them in context, and demonstrate explainable ownership. ==As argued in Section 3.8, the frameworks compared in Table 3 each assume either that the learner starts without a complete artifact or that the artifact's imperfections are visible; Reverse Learning addresses the situation in which neither assumption holds.==

Reverse Learning is also distinct from assessment frameworks such as the AI Assessment Scale (AIAS). The AIAS helps educators communicate and design appropriate levels of generative AI use in assessment tasks, ranging from no AI use to exploratory AI integration (Perkins et al., 2024). Reverse Learning can operate within such assessment levels, but its focus is different: it describes the learner process required to transform AI-generated artifacts into explainable understanding. In this sense, AIAS helps define whether and how AI may be used in an assignment, whereas Reverse Learning explains how learning can occur when AI-generated outputs are used as provisional objects for critique and reconstruction.

# 8. Pedagogical Applications and Assessment

The Reverse Learning Framework can guide assignment design, assessment, and AI policy. Its practical value lies in shifting attention from prohibiting AI use to designing accountable AI use. This orientation aligns with recent assessment design frameworks such as the AI Assessment Scale, which supports educators in making transparent decisions about the appropriate level of generative AI integration in assessment tasks (Perkins et al., 2024). Reverse Learning complements such frameworks by specifying the learner actions and evidence of understanding that should accompany AI-permitted or AI-integrated assignments. In practical terms, Reverse Learning is most useful when AI use is allowed but must be made educationally accountable. It provides a process for documenting how learners moved from generated output to verified and reconstructed understanding. ==As argued in Section 3.4, these assessment structures are not merely measurement instruments; they are the contextual conditions that activate and sustain the critical engagement the framework requires.==

## 8.1 AI Output Critique Assignment

Students submit an AI-generated draft and annotate its strengths, weaknesses, assumptions, missing evidence, and questionable claims. This assignment directly supports learner skepticism. Assessment criteria may include the ability to identify unsupported claims, distinguish fluency from validity, and prioritize needed revisions.

## 8.2 Verification Log

Students document how they verified AI-generated claims. A verification log may include source checks, citation validation, code tests, calculation checks, or comparisons with course materials. Assessment criteria may include source credibility, accuracy of corrections, and explanation of why particular evidence is trustworthy.

## 8.3 Prompting Reflection

Students explain how their prompts evolved and what they learned through iterative prompting. Rather than submitting only final prompts, students reflect on how questioning changed their understanding. Assessment criteria may include progression from generic to targeted prompts, evidence of conceptual clarification, and reflection on misconceptions.

## 8.4 Reconstruction Draft

Students submit a final artifact that has been substantially revised and contextualized. They may also submit a before-and-after comparison showing how the initial AI output changed. Assessment criteria may include conceptual revision, integration of verified evidence, contextual adaptation, and use of the learner's own reasoning.

## 8.5 Oral Defense

Students answer questions about their final artifact without AI assistance. This may be done in class, through video submission, or through a short instructor conference. Assessment criteria may include ability to explain the argument, justify evidence, identify limitations, and respond to alternative interpretations.

## 8.6 Ownership Statement

Students disclose how AI was used and explain what they verified, changed, and learned. This statement shifts disclosure from a compliance act to a learning reflection. Assessment criteria may include transparency, specificity, evidence of human contribution, and demonstration of intellectual responsibility.

Table ==4== translates the process model into assessment design. If Table ==3== clarifies what Reverse Learning is not, Table ==4== clarifies how Reverse Learning can be observed in practice. This table is especially important for instructors and instructional designers because it connects each stage of the framework to evidence that can be submitted, reviewed, or assessed.

Table ==4==. Stage, Evidence, and Assessment Alignment

[TABLE]
Stage | Observable evidence | Assessment approach
AI-Generated Artifact | Initial AI output and prompt | AI output submission
Learner Skepticism | Annotations and questions | Critique rubric
Verification | Source checks and corrections | Verification log
Iterative Prompting | Prompt history and reflection | Prompting reflection
Contextual Integration | Context-specific adaptations | Contextualization rubric
Human Reconstruction | Revised artifact and rationale | Before/after comparison
Explainable Ownership | Oral defense or ownership statement | Defense rubric / reflective memo
[/TABLE]

Table ==5== positions Reverse Learning in relation to AI assessment policy. The purpose is not to replace the AIAS, but to show how Reverse Learning can complement it. AIAS helps define the permitted level of AI use in an assessment task; Reverse Learning helps define what learners should do with AI-generated outputs when such use is permitted.

Table ==5==. Alignment Between AIAS and Reverse Learning

[TABLE]
Assessment question | AIAS contribution | Reverse Learning contribution
Is AI permitted? | Defines the level of GenAI use | Provides a process for accountable use
How should AI use be disclosed? | Clarifies expectations | Turns disclosure into an ownership statement
How can assessment remain valid? | Supports assessment redesign | Requires evidence of verification and reconstruction
What should educators evaluate? | Clarifies AI integration level | Evaluates learner judgment and explainable ownership
[/TABLE]

==# 9. Boundary Conditions, Disciplinary Variation, and Limitations==

==Like any conceptual framework, Reverse Learning has boundary conditions: settings in which its assumptions hold and settings in which they do not. Specifying these conditions is essential both for responsible implementation and for the empirical work proposed in Section 10.==

==The framework's core stages take substantially different forms across disciplines because what verification and reconstruction mean differs across epistemic cultures. In STEM domains, many AI-generated claims are directly testable: code can be executed, calculations can be checked, and derivations can be traced. Verification is comparatively fast and objective, and the inquiry loop of Proposition 2 can cycle quickly. In the humanities, verification is interpretive rather than executable: learners must assess whether sources exist and say what the artifact claims they say, whether interpretations are defensible, and whether arguments cohere—judgments that require deliberation and disciplinary enculturation rather than testing. In the social sciences, verification confronts contested evidence bases, methodological pluralism, and context-dependent findings, so learners must evaluate not only whether a claim is supported but by what kind of evidence and with what generalizability. Instructors should therefore calibrate verification expectations and scaffolds to their discipline's evidentiary norms rather than importing a single verification template across domains. Reconstruction varies similarly: rebuilding a proof, reorganizing an interpretive argument, and recontextualizing a policy analysis are different cognitive acts, even though all three close the fluency–validity gap in the sense of Section 3.8.==

==Several boundary conditions limit the framework's applicability. First, Reverse Learning presupposes verifiable content. Tasks whose value lies primarily in personal expression or original creative production offer little for verification to grip, although skepticism and reconstruction may still apply to craft-level choices. Second, the framework presupposes access to verification resources—libraries, documentation, data, or expert feedback—and adequate time; in resource-poor or severely time-constrained settings, assigning Reverse Learning without these supports invites superficial compliance. Third, as developed in Section 6, the framework presupposes minimal prerequisite competencies, and below that threshold it requires heavily scaffolded implementation. Fourth, the framework fits low-stakes, high-volume tasks poorly: when the cost of full engagement exceeds any reasonable value the task carries, expectancy-value dynamics predict abbreviated engagement (Section 3.4), and instructors should either raise the stakes or not expect the full cycle.==

==Three limitations of the present article should also be acknowledged. First, the framework is conceptual and has not yet been empirically validated; the propositions in Section 5 are stated so that they can be tested, and the research agenda in Section 10 specifies how. Second, the framework's assessment practices—particularly oral defenses and instructor questioning—are resource-intensive at scale, and their feasibility in large-enrollment settings remains an open implementation question. Third, the framework addresses individual learners' engagement with AI-generated artifacts; collaborative and team-based variants, in which skepticism and verification are socially distributed, require additional theorization, potentially drawing on socially shared regulation of learning (Järvelä et al., 2023).==

# 10. Research Agenda

Because this article proposes a conceptual framework, empirical research is needed to test and refine it. The framework should be treated as a design hypothesis: if learners are required to question, verify, prompt, contextualize, reconstruct, and explain AI-generated artifacts, then AI-assisted work is more likely to support conceptual understanding than passive delegation. ==The propositions in Section 5.1 sharpen this hypothesis into testable claims about mechanism, and the boundary conditions in Section 9 identify the moderators that studies should sample across.== Four research directions are particularly important.

RQ1. Learner Understanding. How does structured Reverse Learning affect learners' conceptual understanding compared with unstructured AI-assisted writing? Future studies could compare learners who complete structured Reverse Learning assignments with learners who use AI without explicit verification and reconstruction requirements. Possible outcome measures include concept explanation quality, transfer tasks, and oral defense scores.

RQ2. Metacognition ==and Activation==. How does iterative prompting within Reverse Learning influence learners' metacognitive awareness==, and what dispositional, contextual, and task-level conditions activate and sustain learner skepticism (Section 3.4)?== Researchers could analyze prompt logs, reflective journals, and metacognitive awareness measures to examine whether learners become more aware of what they know, what they do not know, and what they need to verify==, and could test whether announced ownership-based assessment shifts learners from efficiency-oriented to inquiry-oriented AI use, as expectancy-value theory predicts.==

RQ3. Verification Behavior. What scaffolds help learners move from passive acceptance of AI outputs to active verification? Design-based research could test scaffolds such as verification logs, source comparison templates, AI hallucination checklists, and instructor modeling==, and could examine how scaffold effectiveness varies with learner expertise, as the expertise reversal effect predicts (Kalyuga, 2007), and across the disciplinary contexts described in Section 9.==

RQ4. Explainable Ownership. How can educators validly assess learner ownership in AI-mediated assignments? Future research could develop and validate rubrics for oral defense, ownership statements, revision rationales, and transfer tasks. ==The three-layer conceptualization in Section 5.2 provides a starting point for construct validation: measures of accountable authorship, epistemic ownership, and identity-level ownership should be distinguishable, and epistemic ownership should predict performance on transfer tasks better than the other two layers.==

Together, these research directions would help determine when Reverse Learning supports learning, when it fails, and what instructional supports are necessary. They would also help clarify whether explainable ownership can be assessed reliably across disciplines, learner populations, and assignment types.

# 11. Discussion: From Detection-Based Ethics to Ownership-Based Learning Design

The Reverse Learning Framework proposes a shift in how educators think about AI ethics, assessment, and learning design. The framework does not reject disclosure, policy, or assessment controls. Rather, it argues that such controls are insufficient unless they are paired with learning designs that make understanding visible.

Many current approaches begin with detection: Did the student use AI? Can the institution identify AI-generated text? Should AI use be prohibited, disclosed, or penalized? These questions are not irrelevant, but they are incomplete. A detection-based approach treats AI use primarily as a compliance problem. An ownership-based approach treats AI use as a learning design problem. It asks whether learners can explain, verify, contextualize, and defend AI-assisted work. ==Detection-based approaches are also structurally unable to distinguish pseudo-competence from genuine competence: a polished artifact looks the same whether or not its holder understands it. Ownership-based assessment addresses precisely this blind spot.==

This argument is consistent with assessment reform efforts that move beyond simple prohibition. The AI Assessment Scale, for example, provides a practical structure for clarifying the role of AI in assessment and supporting dialogue between educators and students about appropriate use (Perkins et al., 2024). Reverse Learning extends this assessment-design conversation by focusing on the learner's epistemic work after AI has produced an output.

The framework also addresses a likely objection: if AI systems become more accurate, will Reverse Learning still be necessary? The answer is yes. Better AI may reduce some errors, but it does not eliminate the need for human judgment. ==Indeed, increasing accuracy widens rather than closes the fluency–validity gap in one crucial respect: the more reliable AI output becomes, the weaker the learner's incentive to scrutinize it, and the more concealed the remaining defects become (Gerlich, 2025).== Learners still need to understand why an answer is valid, how it applies to context, what limitations remain, and how it should be adapted for a particular purpose.

A second objection is that Reverse Learning may simply describe good critical thinking. Critical thinking is central to the framework, but Reverse Learning specifies a distinct AI-mediated pattern: artifact-first learning. Learners begin with machine-generated artifacts and work backward into understanding through structured stages of skepticism, verification, prompting, contextual integration, reconstruction, and ownership. ==As Section 3.8 argues, the framework contributes an explanatory mechanism—the discovery and resolution of the fluency–validity gap—that generic critical thinking accounts do not provide.==

A third objection concerns equity. Learners with stronger prior knowledge may be better positioned to verify and reconstruct AI outputs. This is a serious concern==, and Section 6 addresses it in detail:== Reverse Learning should not be treated as a self-sufficient method that students can perform without support. It requires scaffolds, rubrics, instructor modeling, source access, and opportunities for feedback. Without such supports, Reverse Learning may privilege learners who already possess stronger metacognitive and disciplinary skills. For instructional designers, the implication is clear: AI-integrated assignments should not merely permit or prohibit AI. They should structure the learner's movement from AI-generated output to human-owned understanding.

# 12. Conclusion

Generative AI challenges traditional assumptions about learning, authorship, and assessment. If learners use AI to bypass thinking, then AI threatens education. But if learners use AI-generated artifacts as objects for critique, verification, dialogue, contextualization, and reconstruction, then AI can become a catalyst for learning. The Reverse Learning Framework offers a model for designing this second possibility. It proposes that AI-generated outputs should not be treated as final answers, but as provisional learning objects that learners must question, verify, contextualize, reconstruct, and explain. In doing so, the framework shifts attention from detecting AI use to designing for learner ownership.

In the age of generative AI, learning may increasingly begin after an answer has been generated. The presence of an AI-produced artifact does not end the learning process; it can begin a new one. Reverse Learning is therefore not the automation of learning. It is the humanization of AI-assisted learning.

# AI Use Disclosure

During the preparation of this manuscript, the author used generative AI tools for brainstorming, outlining, language refinement, source mapping, and critical dialogue. The author reviewed, revised, verified, and takes responsibility for all arguments, interpretations, citations, and conclusions. No generative AI tool is listed as an author.

# References

Anthropic. (2026a). How AI assistance impacts the formation of coding skills. https://www.anthropic.com/research/AI-assistance-coding-skills

Anthropic. (2026b). Anthropic Education Report: The AI Fluency Index. https://www.anthropic.com/research/AI-fluency-index

Bearman, M., Ryan, J., & Ajjawi, R. (2023). Discourses of artificial intelligence in higher education: A critical literature review. *Higher Education*, *86*, 369–385. https://doi.org/10.1007/s10734-022-00937-2

==Cacioppo, J. T., & Petty, R. E. (1982). The need for cognition. *Journal of Personality and Social Psychology*, *42*(1), 116–131. https://doi.org/10.1037/0022-3514.42.1.116==

==Chan, C. K. Y., & Zhou, W. (2023). An expectancy value theory (EVT) based instrument for measuring student perceptions of generative AI. *Smart Learning Environments*, *10*, Article 64. https://doi.org/10.1186/s40561-023-00284-4==

Chi, M. T. H., & Wylie, R. (2014). The ICAP framework: Linking cognitive engagement to active learning outcomes. *Educational Psychologist*, *49*(4), 219–243. https://doi.org/10.1080/00461520.2014.965823

Chikofsky, E. J., & Cross, J. H., II. (1990). Reverse engineering and design recovery: A taxonomy. *IEEE Software*, *7*(1), 13–17. https://doi.org/10.1109/52.43044

==Chinn, C. A., Buckland, L. A., & Samarapungavan, A. (2011). Expanding the dimensions of epistemic cognition: Arguments from philosophy and psychology. *Educational Psychologist*, *46*(3), 141–167. https://doi.org/10.1080/00461520.2011.587722==

Cotton, D. R. E., Cotton, P. A., & Shipway, J. R. (2024). Chatting and cheating: Ensuring academic integrity in the era of ChatGPT. *Innovations in Education and Teaching International*, *61*(2), 228–239. https://doi.org/10.1080/14703297.2023.2190148

Eaton, S. E. (2023). Postplagiarism: Transdisciplinary ethics and integrity in the age of artificial intelligence and neurotechnology. *International Journal for Educational Integrity*, *19*, Article 23. https://doi.org/10.1007/s40979-023-00144-1

==Eccles, J. S., & Wigfield, A. (2020). From expectancy-value theory to situated expectancy-value theory: A developmental, social cognitive, and sociocultural perspective on motivation. *Contemporary Educational Psychology*, *61*, Article 101859. https://doi.org/10.1016/j.cedpsych.2020.101859==

Flavell, J. H. (1979). Metacognition and cognitive monitoring: A new area of cognitive-developmental inquiry. *American Psychologist*, *34*(10), 906–911. https://doi.org/10.1037/0003-066X.34.10.906

Flipped Learning Network. (2014). The four pillars of F-L-I-P. https://flippedlearning.org/definition-of-flipped-learning/

==Gerlich, M. (2025). AI tools in society: Impacts on cognitive offloading and the future of critical thinking. *Societies*, *15*(1), Article 6. https://doi.org/10.3390/soc15010006==

Jaakkola, E. (2020). Designing conceptual articles: Four approaches. *AMS Review*, *10*, 18–26. https://doi.org/10.1007/s13162-020-00161-0

==Järvelä, S., Nguyen, A., & Hadwin, A. (2023). Human and artificial intelligence collaboration for socially shared regulation in learning. *British Journal of Educational Technology*, *54*(5), 1057–1076. https://doi.org/10.1111/bjet.13325==

==Kalyuga, S. (2007). Expertise reversal effect and its implications for learner-tailored instruction. *Educational Psychology Review*, *19*(4), 509–539. https://doi.org/10.1007/s10648-007-9054-3==

Kapur, M. (2008). Productive failure. *Cognition and Instruction*, *26*(3), 379–424. https://doi.org/10.1080/07370000802212669

Kapur, M. (2016). Examining productive failure, productive success, unproductive failure, and unproductive success in learning. *Educational Psychologist*, *51*(2), 289–299. https://doi.org/10.1080/00461520.2016.1155457

Kasneci, E., Sessler, K., Küchemann, S., Bannert, M., Dementieva, D., Fischer, F., Gasser, U., Groh, G., Günnemann, S., Hüllermeier, E., Krusche, S., Kutyniok, G., Michaeli, T., Nerdel, C., Pfeffer, J., Poquet, O., Sailer, M., Schmidt, A., Seidel, T., ... Kasneci, G. (2023). ChatGPT for good? On opportunities and challenges of large language models for education. *Learning and Individual Differences*, *103*, Article 102274. https://doi.org/10.1016/j.lindif.2023.102274

==Knoth, N., Tolzin, A., Janson, A., & Leimeister, J. M. (2024). AI literacy and its implications for prompt engineering strategies. *Computers and Education: Artificial Intelligence*, *6*, Article 100225. https://doi.org/10.1016/j.caeai.2024.100225==

Long, D., & Magerko, B. (2020). What is AI literacy? Competencies and design considerations. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (Article 598, pp. 1–16). Association for Computing Machinery. https://doi.org/10.1145/3313831.3376727

Lodge, J. M., Yang, S., Furze, L., & Dawson, P. (2023). It's not like a calculator, so what is the relationship between learners and generative artificial intelligence? *Learning: Research and Practice*, *9*(2), 117–124. https://doi.org/10.1080/23735082.2023.2261106

Mollick, E. R., & Mollick, L. (2023). Assigning AI: Seven approaches for students, with prompts. *arXiv*. https://doi.org/10.48550/arXiv.2306.10052

Ng, D. T. K., Leung, J. K. L., Chu, S. K. W., & Qiao, M. S. (2021). Conceptualizing AI literacy: An exploratory review. *Computers and Education: Artificial Intelligence*, *2*, Article 100041. https://doi.org/10.1016/j.caeai.2021.100041

Perkins, M., Furze, L., Roe, J., & MacVaugh, J. (2024). The Artificial Intelligence Assessment Scale (AIAS): A framework for ethical integration of generative AI in educational assessment. *Journal of University Teaching and Learning Practice*, *21*(6). https://doi.org/10.53761/q3azde36

==Pierce, J. L., Kostova, T., & Dirks, K. T. (2003). The state of psychological ownership: Integrating and extending a century of research. *Review of General Psychology*, *7*(1), 84–107. https://doi.org/10.1037/1089-2680.7.1.84==

==Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences*, *20*(9), 676–688. https://doi.org/10.1016/j.tics.2016.07.002==

Scardamalia, M., & Bereiter, C. (2006). Knowledge building: Theory, pedagogy, and technology. In R. K. Sawyer (Ed.), *The Cambridge handbook of the learning sciences* (pp. 97–118). Cambridge University Press.

UNESCO. (2023). Guidance for generative AI in education and research. UNESCO. https://unesdoc.unesco.org/ark:/48223/pf0000386693

WAME. (2023). Chatbots, generative AI, and scholarly manuscripts: WAME recommendations on chatbots and generative artificial intelligence in relation to scholarly publications. https://wame.org/page3.php?id=106

Wiggins, G., & McTighe, J. (2005). *Understanding by design* (Expanded 2nd ed.). ASCD.

==Zimmerman, B. J. (2000). Attaining self-regulation: A social cognitive perspective. In M. Boekaerts, P. R. Pintrich, & M. Zeidner (Eds.), *Handbook of self-regulation* (pp. 13–39). Academic Press. https://doi.org/10.1016/B978-012109890-2/50031-7==

==Zimmerman, B. J. (2002). Becoming a self-regulated learner: An overview. *Theory Into Practice*, *41*(2), 64–70. https://doi.org/10.1207/s15430421tip4102_2==
