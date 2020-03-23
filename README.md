*Last updated: March 22, 2020 08:00 ET*

# Making NP swabs

As clinical laboratories around the world have begun testing for Covid-19, we have encountered a new crisis: a shortage of the swabs required to obtain the necessary sample. These are called nasopharyngeal swabs, or NP swabs for short.

**The goal of this repository is sharing [methods](#design), [testing procedures](#testing), and [results](#results) required to manufacture NP swabs locally/everywhere at volumes of thousands per day, until standard manufacturers can make and deliver more.**

Because the crisis is **now,** the goal is to re-create versions of the swabs already in use (as opposed to creating better/fundamentally different redesigns).

The files in this repo contain some information to get started. **This includes .stl files that you can modify/print (see [design_files](design_files/) above).**

If anyone has any questions, please reach out to any of the contributors here or to Dr. Ramy Arnaout, MD, DPhil, at rarnaout@bidmc.harvard.edu.

Anything you find here is free for use for all.

If you want us to test swab materials at BIDMC we are happy to, please contact Cody Callahan at BIDMC (calla4@bidmc.harvard.edu). 

For efficiency, we strongly suggest you find local partners either in addition or instead for [testing](#testing) and ask one of [us](#contact) for write access to share your [results](#results) here on the repo.


## Contents

- [Basic description of an NP swab](#design)
- [Requirements](#reqs)
- [Anti-requirements: What's not required](#not-reqs)
- [List of known acceptable swabs](#acceptable-swabs)
- [Manufacturing approaches](#approaches)
- [Flock](#flock)
- [Materials and adhesives](#adhesive)
- [Packaging](#packaging)
- [Testing procedures](#testing)
- [Results](#results)
- [Contact](#contact)

<a name="design"></a>
## Basic description of an NP swab

(Click images for larger versions)

<img src="img/adult_np_swab_procedure.png" width=40%><img src="img/commercial-swab.png" width=20%><img src="img/copan_flocked_swab_micro_1.png" width=40%>

<img src="img/copan_flocked_swab_macro.png" width="100%">

An NP swab is a flexible stick around 15cm in length that goes up your nose to the back of the nasal cavity (see [movie](https://www.youtube.com/watch?v=hXohAo1d6tk&feature=youtu.be&t=40)). It is swept or twirled around to brush or wick up secretions, which carry Covid-19 virus particles. The swab comes out of the nose and goes into a vial that contains fluid (viral transport medium, VTM, for which there are now recipes [from IU](Other_Docs/VTM_IU_recipe.pdf) and [the CDC](Other_Docs/CDC_Viral-Transport-Medium.pdf)). The vial gets capped and sent for processing.

There are **two parts**: a bristled **bulb** end (above) and a **shaft**. The bristles in the above are nylon.

The bulb looks like it would be fluffy to the touch but it is not: the bristles are short enough that it feels more like hard foam.

Often the shaft itself has a thin **neck**, for flexibility, and a thicker **handle**. The handle is often **scored**---a weak point in the shaft---where you can break it off so the bristled part stays in the vial; the handle is then thrown away.

**Score at \~7 cm from bulb tip.** The location of the score (distance from the bulb along the handle) must be smaller than the height of the vial you use. For example, for the vials for use with Copan 480C swabs, the breakpoint is 7cm; for [15-](https://www.fishersci.com/shop/products/falcon-15ml-conical-centrifuge-tubes-5/p-193301) or [50-mL](https://www.fishersci.com/shop/products/falcon-50ml-conical-centrifuge-tubes-2/p-193321) conical tubes (of the kind used routinely in biomedical research and sold by many manufacturers), 11 cm will do. It is mildly easier for handling if the score is close to the height of the vial but the requirement is that it is less than the height.

Helpful target measurements:

- Diameter of head with bristles: 3mm
- Diameter of head without bristles: \~2mm
- Diameter of neck: 1mm
- Diameter of handle: 2.5mm
- Length of bulb: 15mm
- Length that will be submerged in [transport medium](#pcr): \~30mm


<a name="reqs"></a>
# Requirements

## Medical requirements

-	**Stiffness, flexibility.** Wand is stiff enough to push to the back of the nasal cavity but flexible enough to get up the nose and will bend when it hits resistance instead of stabbing people (for reference, swabs are a little more flexible than the tiny straws used for coffee, and somewhat similar to the inside tube that holds the ink when you take apart a Bic ballpoint pen). **Swab must not snap off in patient's nose**

-	**Tip.** Ideally, the bulb end is *flocked* (see below): it has lots of tiny bristles perpendicular to the wand (see close-up above). The bristles provide for a high surface-area-to-volume and helps both wick secretions onto the bristle and liberate particles when put in the transport medium. Perpendicularity is a nice-to-have that we believe may improve yield slightly but requires electrostatic deposition; even random orientation of flock should work fine

-	Bristles or collecting substrate (including any adhesive) must be firmly attached and not get left behind in the nasal cavity. Similarly no part of the swab should break off or get left in the nasal cavity

-	[Materials](#adhesive) cannot inhibit [PCR](https://en.wikipedia.org/wiki/Reverse_transcription_polymerase_chain_reaction). This means no wood or cotton (although we believe rayon is OK). Nylon and polypropylene seem to be good choices, but start with medical equipment/grade materials if possible since they should be high quality/pure (some additives can be inihibitors).

-	Wand must break off inside the tube – better to be too short than too long.  Wand could be manually scored to create a weak point. If not, might need scissors at point of care (not ideal)

For more technical requirements, see [Design Constraints](Other_Docs/Design%20Constraints.md)


<a name="not-reqs"></a>
## Anti-requirements: What's not required

-	Sterility. Not a major concern for most uses; only for immunocompromised (in which case the ability to decontaminate by [autoclaving](https://en.wikipedia.org/wiki/Autoclave) or ethanol or isopropanol bath is needed). The air and the nose are already non-sterile and the PCR assay is specific enough to ignore most contaminants (as long as other Covid-19 contaminated things/people don’t come in contact with it and it doesn’t pick up PCR inhibitors)

-	Labor intensive is ok, to fill short term needs. There are students and researchers out of school and lab who are willing to volunteer to hand-assemble these from inoculation loops, adhesive, and wicking substrate #studentArmy


<a name="acceptable-swabs"></a>
## List of known acceptable swabs

Model what you make after one of these.

Product numbers are listed. Unless otherwise stated, these are from the [FDA approved list](https://www.fda.gov/medical-devices/emergency-situations-medical-devices/faqs-diagnostic-testing-sars-cov-2) current as of **March 20, 2020**. You can look these up online.

**Copan:** 480C *(2)*, 481C *(1)*, 482C *(1)*, 501CS01, 503CS01, 516CS01, 518CS01, 534CS01

**Puritan:** LA-117 *(1)*, 3317-H, 25-3317-H, 25-3316-U, 25-3316-H, 25-3317-U, 25-3318-U, 25-3318-H, 25-3319-H, 25-3320-U, 25-3320-U EMB 100MM, 25-3320-U EMB 80MM, 25-3320-H and 25-3320-H EMB 80MM

*(1)* Preferred, per FDA

*(2)* Acceptable, per BIDMC


<a name="approaches"></a>
## Manufacturing approaches

**We believe the best use of resources is to be creative around copying the template, not redesigning swabs.**

- 3D print a shaft, and attaching flock material via adhesive

- 3D print a shaft with enough definition---either "nubs" along the surface or bristles---to gather secretion from the nasopharynx.

For more detail on ideas not yet investigated, including repurposing unrelated items like cosmetics applicators, or using other items common in labs, see [Other Approaches](Other_Docs/Repurposing_Approach.md)

### 3D-print shaft + adhesive + swab

- 3D print a wand with the appropriate form factor (e.g. see the picture above and the .stl files)
- dip bulb in adhesive (we are working on appropriate adhesives)
- dip sticky bulb in [flock](#flock)
- shake/blow/rinse off excess flock
- (if needed) dip in 70% ethanol for sterilization

(This is like how you'd solve this problem if you were in elementary school.) Currently we have no proven way to automate the last three steps so we are envisioning a "student army." Better ideas welcome.

### 3D-print entire swab

The ability to print a swab complete with bristles or equivalent saves the steps for requiring adhesive and [flock](#flock). 

Stereolithography 3D printed prototypes by **OPT Industries** look promising (see example bulbs, below---note in this approach the whole swab including bulb is printed at once, on their own DLP/SLA machines); we are testing materials now.
<img src="img/carbon_formlabs_bristles.png" width=100%>
<img src="img/OPT_industries/OPTIndustries_full_Swab_1.jpg" width=33%> <img src="img/OPT_industries/OPTIndustries_full_Swab_2.jpg" width=33%>



<a name="flock"></a>
## Flock

"Flock" is the name of the bristle material. It can be ordered from e.g. www.flockit.com as a powder. The below information comes from extremely helpful conversations with them and Celluseude, the manufacturer.

- The nylon flock on the tip of the picture is 3 [denier](https://en.wikipedia.org/wiki/Units_of_textile_measurement#Denier) (3 [dtex](https://en.wikipedia.org/wiki/Units_of_textile_measurement#Denier))

- The flock on the flocked swab above was likely applied using electrostatic deposition: flock coated with something positively charged, shaft coated with adhesive and electrically grounded. We do not need to do this: the previous version of swabs, still widely in use, have matted flock and they work well enough (slightly lower sensitivity but clinically for now we'll take it)

- In general acrylic is used as the adhesive for flock, but be aware that acrylic is a **known PCR inhibitor** (see below). Decision point is rinse a lot to remove loose acrylic vs. just use something safer. Apparently Elmer's has something of the same problem.

- The only colors you should consider for the nylon are black and white, with preference for white. Black has some inorganic compound that is assumed to be PCR-safe; white has titanium inside the fiber but not on the surface so is more likely PCR safe. (White is the purest nylon.) Colored nylons have various ionic or covalent groups on the outside, which are unnecessary complications.

- Rayon is also safe to use



<a name="shaft"></a>
## Shaft

This is the easiest part to 3D-print.

It should be able to be easily broken off, so that only the tip with the patient's nasal secretion is in a specimen container.  Easy break-off may be accomplished via scoring.


<a name="packaging"></a>
## Packaging

As we get closer to having swabs, we will want a solution for packaging. Ideally at least semi-sterile, definitely single-swab packaging.

Packaging must be RNase-free for the test to work.

Possibly will want to fork this process: more sterile for immunocompromised patients, less for others.

Current best thought is to package manually in sterile hoods:

- begin with swabs in ethanol vat/bucket
- spread and cut plastic wrap
- leave under UV light in hood (*1*)
- take swab out of ethanol and place horizontally on strip of plastic to dry
- **When dry,** fold plastic over swab
- packing done

(*1*) UV is not expected to destroy plastic on timescales of under a few hours

Thoughts on throughputting this?


<a name="adhesive"></a>
## Materials and adhesives

Adhesives will need to adhere the two substances (printed shaft + flock) and will need to not leave behind anything in the nasal cavity / nasopharynx when used.

Some materials and adhesives inhibit PCR (see [testing protocol](#pcr) below). See the [Kodzius 2012](Other_Docs/kodzius2012.pdf) and [forensicGEM's work](Other_Docs/forensicGEM_Tissue_AppNote_TapeInhibition.pdf) for details.

From those files:

### Safe materials (any red bar above \~50 in [Kodzius Fig. 3](Other_Docs/kodzius2012.pdf)): (*1*)
- polypropylene
- PTFE
- PDMS
- SiO2 quartz
- Pyrex glass
- Soda-lime glass
- NOA68

### Unsafe materials:
- PMMA
- Silicon
- SiO2 5600A
- ITO glass
- SU-8
- NOA61

### Unknown:
- metals including steel and aluminum (in principle these stick to polymerase, but the effect size depends on the form factor so we don't know yet)
- polycryl resin (we believe the monomers are not PCR safe, but if cured and washed could be ok; we will test)

### Safe adhesives (from Kodzius Fig. 3 and from forensicGEM document Fig. 1):
- Wax (Tm 80C)
- the glue used in Scotch Magic Tape 810
- the glue used in Scotch Crystal Clear Tape
- the glue used in Scotch Mailing Tape
- the glue used in Scotch Storage Freezer Tape
- the glue used in Scotch Transparent Tape 550
- the glue used in Sellotape Brown Packaging Tape
- the glue used in Applied Biosystems MicroSeal Adhesive Film

### Unsafe adhesives:
- Wax (Tm <80C)
- Epoxy glue
- Acrylic glue
- the glue used in Scotch Masking Tape (made in Canada or Taiwan)
- the glue used in Scotch Removable Magic Tape 811
- the glue used in Sellotape Diamond Ultra Clear
- the glue used in Sellotape Invisible Permanent Write-on
- the glue used in Sellotape Cellulose Easy-Tear Tape
- the glue used in Sellotape Double-Sided Tape
- the glue used in 3M PostIt notes

(*1*) Some materials can in principle be used as adhesives, e.g. PDMS


<a name="testing"></a>
## Testing procedures

We propose/are using a three-step testing procedure:

- expert review
- sufficient collection of material
- PCR compatibility

### Expert review

There is no substitute for having a health professional who actively uses NP swabs evaluate your prototype. If such an expert says it "looks good," that is enough to pass this test (see [Results](#results) below)

Two frequently-asked questions are re: length and flexibility. For length, our current recommendation is 15cm. For flexibility: if you have a [swab to compare to](#acceptable-swabs), that is the best way to guage flexibility. If not: your swab should as flexible as the inside part of a standard Bic ball-point pen (the tube that contains the actual ink, when you take the pen apart).

### Sufficient collection of material

For collection of material:

- swirl against the inside of your cheek (make sure the swab is clean first)
- rub on a slide
- perform a [Gram stain](https://en.wikipedia.org/wiki/Gram_stain)
- visualize under a microscope
- take picture through ocular
- compare picture to control we made using an actual NP swab (to be posted soon)

The viral particles we are looking to collect are smaller than bacteria, but if you collect a fair number of bacteria, that is considered Ok for now (ask a microbiologist or microbiology tech, and we will provide a picture of what we think is acceptable when we can).

<a name="pcr"></a>
### PCR compatibility

It is essential to confirm that nothing in the final product (material ± adhesive) inhibits RT-PCR, on which current tests are based (details of the reagents differ somewhat from assay to assay; we will post). A testing protocol is as follows. Note because this has a substantial incubation time, **it is a good idea to start testing materials before prototypes are done, if possible.**

- incubate bulb in 3mL Viral Transport Medium (VTM; [recipe courtesy IU](Other_Docs/VTM_IU_recipe.pdf)) overnight (12 hr)
- spike the VTM with positive control (*1*)
- aliquot 700µl for testing
- run RT-PCR (*2*) (*3*)

(*1*) If you are working with clinical labs who have the bandwidth, they can use inactivated Covid-19 particles that are used clinically as the positive control any virus. If not, and you are/have access to colleagues in a virology lab working with encapsulated virus, that can be used. If not, then any mRNA.

(*2*) Many protocols and reagents are proprietary, but many hospitals have developed their own laboratory-developed tests (LDTs) that may have made their protocols publicly available. If you find and [forward](#contact) we will post.

(*3*) An RNA extraction step [may not be required](https://www.biorxiv.org/content/10.1101/2020.03.20.001008v1)

See also [this FDA page](https://www.fda.gov/medical-devices/emergency-situations-medical-devices/faqs-diagnostic-testing-sars-cov-2) for speific testing details.


<a name="results"></a>
## Results

As materials and designs (including existing swabs) get tested, we will record passing results [here](Results/np_swab_results.xlsx). See images in the appropriate subfolders in the [img/ directory.](img/)

<img src="img/results.png">

Please organize entries into the following fields. We plan to turn into a (sortable, updatable) table, but don't wait for that: just upload entries (separating each entry by line breaks). Please **copy** the below for each entry (i.e., don't overwrite it). If you need help [contact us](#contact).
___

### ENTRY TEMPLATE

#### Identifier
This is a unique identifier, ideally including the source's name

#### Date of test

#### Test site
E.g., BIDMC

#### Picture
Please take a high-resolution picture of the **entire** item provided.

#### Material
Please describe all (known) materials in the bulb head, including plastic, any adhesive, and any flock

#### Process
Please include a brief description of the design process that an expert would understand well enough to reproduce. For repurposed swabs, write "commercial."

#### Creator (contact info and company)
How to contact the creator for questions/further development

#### Link to stl and cad files
Please send .stl and CAD files, which we will post.

#### Test 1: NP swab user evaluation (eg an ID doc), with comments
If passes, write "Pass". If fails, write "Fail" and give a brief reason why. Should be filled out by someone who has experience actually using NP swabs in a clinical context. Please leave the name of this person.

#### Test 2: Collection test
If a Gram stain of the (inner) cheek made from the swab shows material broadly consistent with our control, then write "Pass". If not, "Fail" and give reason (too abrasive, did not pick up material, etc.)

#### Test 3: PCR compatibility (and which protocol used)
As above, "Pass" vs. "Fail". Please indicate the protocol used. You can post the protocol in the Testing/ directory, and link to it here

___


#### Identifier
This is a unique identifier, ideally including the source's name

#### Date of test

#### Test site
E.g., BIDMC

#### Picture
Please take a high-resolution picture of the **entire** item provided.

#### Material
Please describe all (known) materials in the bulb head, including plastic, any adhesive, and any flock

#### Process
Please include a brief description of the design process that an expert would understand well enough to reproduce. For repurposed swabs, write "commercial."

#### Creator (contact info and company)
How to contact the creator for questions/further development

#### Link to stl and cad files
Please send .stl and CAD files, which we will post.

#### Test 1: NP swab user evaluation (eg an ID doc), with comments
If passes, write "Pass". If fails, write "Fail" and give a brief reason why. Should be filled out by someone who has experience actually using NP swabs in a clinical context. Please leave the name of this person.

#### Test 2: Collection test
If a Gram stain of the (inner) cheek made from the swab shows material broadly consistent with our control, then write "Pass". If not, "Fail" and give reason (too abrasive, did not pick up material, etc.) Note: BIDMC protocol does not include adding fluid.

#### Test 3: PCR compatibility (and which protocol used)
As above, "Pass" vs. "Fail". Please indicate the protocol used. You can post the protocol in the Testing/ directory, and link to it here

___


<a name="contact"></a>
## Contact us

We want to emphasize this is a **group effort** with literally scores of people working on this right now; if you're reading this, you're probably one of them. If you have something to contribute, please contact Dr. Ramy Arnaout, MD, DPhil, at rarnaout@bidmc.harvard.edu.

Note there's also now a [Slack channel](https://join.slack.com/t/rapidmanufact-iop4498/shared_invite/zt-cykndes6-XtxzG~8bkji64M3wTVWiOw).

