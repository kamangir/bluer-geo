# 🌐 copernicus

the `copernicus` catalog covers [Copernicus Data Space Ecosystem - Europe's eyes on Earth](https://dataspace.copernicus.eu/). see [datacube](../) for usage instructions.

 - [api](https://catalogue.dataspace.copernicus.eu/stac)
 - [aws access](https://documentation.dataspace.copernicus.eu/APIs/S3.html)
 - [docs](https://documentation.dataspace.copernicus.eu/APIs/STAC.html)
 - [home](https://dataspace.copernicus.eu/)

## ⚠️ issues

⚠️ "Too Many Requests" error likely.

## query

```bash
@catalog query copernicus help
```
```bash
@catalog query copernicus \
	[dryrun,sentinel_2,select,upload] \
	[ingest,~copy_template,dryrun,overwrite,scope=<scope>,upload] \
	[-|<object-name>] \
	[--bbox <-122.88,51.73,-122.68,51.93>] \
	[--count <10>, -1: all] \
	[--datetime <2024-07-30/2024-08-09>, more: https://documentation.dataspace.copernicus.eu/APIs/STAC.html#search-items-by-datetime] \
	[--keyword <keyword>] \
	[--lat <51.83>] \
	[--lon <-122.78>] \
	[--radius <0.1>]
 . copernicus/sentinel_2 -query-> <object-name>.
   scope: @datacube ingest help.
```

## case study: Miduk copper mine

```bash
@select geo-watch-$(@@timestamp)
@geo watch - \
  target=Miduk-2 - \
  to=local - - .
@assets publish \
  extensions=png+gif,push .
```


| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/geo-watch-2025-05-23-2ck64x/geo-watch-2025-05-23-2ck64x.gif?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/geo-watch-diff-2025-05-23-2j8p1f/geo-watch-diff-2025-05-23-2j8p1f.gif?raw=true) |

 - [Google Maps](https://maps.app.goo.gl/vaVBoDgci6kJP2KEA): `lat: 30.4167"N`, `lon: 55.1667"E`.

---

using [Miduk](../../watch/targets/md/Miduk.md).

## example run

```bash
@select
@catalog query copernicus sentinel_2 - . \
  --count 10 \
  --datetime 2024-07-30/2024-08-09 \
  --lat  51.83 \
  --lon -122.78

@select $(@catalog query read - . --count 1 --offset 3)
@datacube ingest scope=metadata+rgb .

@publish tar .
```

![image](https://github.com/kamangir/assets/blob/main/blue-geo/chilcotin-query-2024-08-23-v1.png?raw=true)

[datacube-copernicus-sentinel_2-S2A_MSIL1C_20240807T190911_N0511_R056_T10UEC_20240808T002811-SAFE.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/datacube-copernicus-sentinel_2-S2A_MSIL1C_20240807T190911_N0511_R056_T10UEC_20240808T002811-SAFE.tar.gz)

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-183-53e60268d40e)
