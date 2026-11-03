---
content_hash: 1358512a559a17250f0758906b5bca3115117a0cc391094b75e6bd8a8cfaf63d
fetched_at: '2026-06-29T00:11:39.866324+00:00'
page_id: '790644707'
product: rm
source: tdn-rm
title: Secretaria - Parâmetros Gerais 6/7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=790644707
version: 1
---

### Armazenamento de arquivos > Arquivo de algum diretório.

Ao selecionar a opção de tipo de armazenamento como, arquivo de algum diretório, o campo diretório de armazenamento fica habilitado, então deve-se colocar um diretório valido para armazenamento dos arquivos.

Ao selecionar a opção de Arquivo de base de dados, os arquivos serão armazenados no banco de dados e a opção de diretório de armazenamento fica bloqueada.

Ao selecionar a opção de Arquivo no ECM (módulo de gestão de documento do Fluig), opção de diretório de armazenamento fica bloqueada.

Neste parâmetro são salvo os arquivos de reserva de instalação, reserva de recurso, documentos do fiador e documentos do aluno.falseIMPORTANTE!!!

**A partir da Versão 12.1.2209**  
Se a Instituição de ensino, tiver parametrizado o tipo de Armazenamento como: "Arquivo de algum diretório" deverá ser informado o **nome do diretório** (caso estiver com **multitenant habilitado**) ou o **caminho do diretório** (caso estiver com o **multitenant desabilitado**).

**Exemplo** quando o **multitenant** estiver **habilitado**: Imagens\Documentos → esse é o nome do diretório e subdiretório onde os arquivos serão salvos. *Não colocar caminho de pasta  →  ex: c:\arquivos.*

Referência:

**Exemplo** quando o **multitenant** estiver **desabilitado**: C:\Imagens\Documentos → esse é o caminho do diretório e subdiretório onde os arquivos serão salvos.
