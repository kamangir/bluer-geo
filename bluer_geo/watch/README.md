# 🌐 `@geo watch`

watch the planet's story unfold.


```bash
@geo watch help
```
<details>
<summary></summary>

```bash
@geo \
	watch \
	[dryrun] \
	[<query-object-name> | target=<target>] \
	[algo=<algo>,<algo-options>] \
	[~submit | dryrun,to=<runner>] \
	[dryrun,<map-options>] \
	[content=<0.5>,dryrun,~gif,publish,<reduce-options>] \
	[-|<object-name>]
 . watch target -> <object-name>.
   algo: diff | modality
   <algo-options>:
      diff: modality=<modality>,range=<100.0>
      modality: modality=<modality>
   modality: rgb[@<keyword>]
   runner: generic | local
   target: Miduk | Miduk-test
@geo \
	watch \
	map \
	[algo=<algo>,dryrun,~download,modality=<modality>,offset=<offset>,suffix=<suffix>,~upload] \
	[.|<query-object-name>]
 . @geo watch map <query-object-name> @ <offset> -> /<suffix>.
@geo \
	watch \
	query \
	[dryrun,target=<target>,~upload] \
	[.|<object-name>]
 . query target -> <object-name>.
@geo \
	watch \
	reduce \
	[algo=<algo>dryrun,~download,publish,suffix=<suffix>,~upload] \
	[..|<query-object-name>] \
	[.|<object-name>]
 . @geo watch reduce <query-object-name>/<suffix> -> <object-name>.
@targets cat \
	<target-name>
 . cat <target-name>.
@targets cp|copy \
	[-] \
	[..|<object-name-1>] \
	[.|<object-name-2>]
 . copy <object-name-1>/target -> <object-name-2>.
@targets download \
	[open,QGIS]
 . download watch targets.
   object: $BLUE_GEO_WATCH_TARGET_LIST
@targets edit
 . edit watch targets.
   /Users/kamangir/storage/abcli/bluer-geo-target-list-v1/metadata.yaml
   object: $BLUE_GEO_WATCH_TARGET_LIST
@targets get \
	[--delim space] \
	[--including_versions 0] \
	[--target_name <target>] \
	[--what <catalog|collection|exists|one_liner|query_args>]
 . get <target> info.
@targets list \
	[--catalog <catalog>] \
	[--collection <collection>] \
	[--count <count>] \
	[--delim <space>] \
	[--including_versions 0]
 . list targets.
@targets open \
	[~QGIS,template]
 . open targets.
@targets publish \
	[template]
 . publish watch targets.
@targets save \
	[target=all|<target-name>] \
	[.|<object-name>]
 . save target(s) -> <object-name>.
   template: $BLUE_GEO_QGIS_TEMPLATE_WATCH
@targets test
 . test watch targets.
@targets update_template \
	[~download,target=all|<target-name>,~upload]
 . update target template.
@targets upload
 . upload watch targets.
   object: $BLUE_GEO_WATCH_TARGET_LIST
```

</details>


## targets 🎯

- [`targets.geojson`](./targets.geojson)
- list of targets: [bluer-geo-target-list-v1.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/bluer-geo-target-list-v1.tar.gz)
- template: [bluer_geo_watch_template_v1.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/bluer_geo_watch_template_v1.tar.gz)

## example run

```bash
@geo watch - \
  target=Miduk-test - \
  to=local - \
  publish -
```

ℹ️ suffix published gif urls with `-2X` and `-4X` for different scales. example: [1X](TBA/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b.gif), [2X](TBA/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b-2X.gif), [4X](TBA/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b-4X.gif).

## [`Miduk`](./targets/md/Miduk.md)
 - [Google Maps](https://maps.app.goo.gl/vaVBoDgci6kJP2KEA): `lat: 30.4167"N`, `lon: 55.1667"E`.

