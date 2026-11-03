---
content_hash: 831a1d5c3f9bcb3fd70adfe3dc8a436377697ace723764df5ec98a8e04d278b7
fetched_at: '2026-06-29T00:09:37.450337+00:00'
page_id: '425459610'
product: rm
source: tdn-rm
title: Relação de subcampos e seus valores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459610
version: 1
---

**Relação de subcampos e seus valores**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tag** | **Subcampo** | **Descrição** | **Repetível?** | **Valor** | **Campo** | **Observação** |
| 020 | $a | ISBN (somente números) | Não | ISBN do exemplar | LEXEMPLAR.ISBN |  |
|  | $c | Preço | Não | Preço de compra do exemplar | LEXEMPLAR.VALORAQUISICAO |  |
| 022 | $a | ISSN (com hífen) | Não | ISSN da publicação | LPUBLIC.ISSN |  |
| 035 | $a | Número de controle do sistema | Não | Código da publicação e do exemplar | LPUBLIC.CODIGO\_LEXEMPLAR.CODEXEMPLAR |  |
| 040 | $c | Instituição que transcreveu o registro | Não | Nome da unidade bibliotecária | LUNIDADE.UNIDADE |  |
| 041 | $a | Código do idioma no texto | Sim | Abreviação do idioma | LIDIOMAS.ABREVIACAO |  |
| 080 | $a | Número CDU | Não | Classificação da publicação | LPUBLIC.CLASSIFICACAO |  |
|  | $b | Número do autor | Não | Cutter/PHA | LPUBLIC.CUTTERPHA |  |
|  | $x | Subdivisão auxiliar | Sim | Subclassificação da publicação | LPUBLIC.SUBCLASSIFICACAO |  |
|  | $2 | Informação de edição | Não | Número da edição do exemplar | LEXEMPLAR.EDICAO |  |
| 082 | $a | Número CDD | Sim | Classificação da publicação | LPUBLIC.CLASSIFICACAO |  |
|  | $b | Número do autor | Não | Cutter/PHA | LPUBLIC.CUTTERPHA |  |
|  | $2 | Informação de edição | Não | Número da edição do exemplar | LEXEMPLAR.EDICAO |  |
| 84 | $a | Número de classificação | Sim | Classificação da publicação | LPUBLIC.CLASSIFICACAO |  |
|  | $b | Número do autor | Não | Cutter/PHA | LPUBLIC.CUTTERPHA |  |
| 090 | $a | Número de chamada local | Não | Classificação da publicação | LPUBLIC.CLASSIFICACAO |  |
|  | $b | Localização | Não | Número de chamada do exemplar | LEXEMPLAR.LOCALIZACAO |  |
|  | $c | Edição | Não | Número da edição do exemplar | LEXEMPLAR.EDICAO |  |
| 100 | $a | Sobrenome ou prenome do autor | Não | Nome do autor normalizado | LAUTOR.NOME | Somente autores principais da obra (pessoal) |
|  | $d | Datas associadas ao nome | Não | Ano de nascimento - Ano de morte | LAUTOR.ANONASC - LAUTOR.ANOFAL |  |
| 110 | $a | Nome da entidade ou lugar | Não | Nome do autor entidade | LAUTOR.NOME | Somente autores principais da obra (institucional) |
| 130 | $a | Título uniforme | Não | Título uniforme da publicação | LPUBLIC.TITULOUNIF |  |
|  | $f | Data da obra | Não | Ano da publicação | LPUBLIC.ANO |  |
|  | $l | Língua da obra | Não | Idioma da publicação | LIDIOMAS.IDIOMA |  |
| 240 | $a | Título uniforme | Não | Título uniforme da publicação | LPUBLIC.TITULOUNIF |  |
|  | $f | Data da obra | Não | Ano da publicação | LPUBLIC.ANO |  |
|  | $l | Língua da obra | Não | Idioma da publicação poe extenso | LIDIOMAS.IDIOMA |  |
| 245 | $a | Título | Não | Título principal da obra | LPUBLIC.TITULO |  |
|  | $b | Títulos paralelos | Não | Subtítulo | LPUBLIC.SUBTITULO |  |
|  | $c | Autores | Não | Nome do autor normalizado | LAUTOR.NOME |  |
| 246 | $a | Título | Não | Título equivalente | LPUBLIC.TITULOEQUIV |  |
| 250 | $a | Edição | Não | Número da edição do exemplar | LEXEMPLAR.EDICAO |  |
|  | $b | Informações adicionais | Não | Complemento da edição | LEXEMPLAR.EDTCOMPL |  |
| 256 | $a | Características do arquivo | Não | Tipo de arquivo e tamanho | LPUBLIC.TIPOARQ (LPUBLIC.TAMANHO, LPUBLIC.VERSAO) |  |
| 260 | $a | Local de publicação | Sim | Local da publicação | LLOCALPUB.LOCAL |  |
|  | $b | Editor ou publicador | Sim | Nome da editora | LEDITORA.EDITOR |  |
|  | $c | Data de publicação | Sim | Ano do exemplar | LEXEMPLAR.ANO |  |
| 300 | $a | Extensão | Sim | Número de páginas | LEXEMPLAR.NUMPAGINA |  |
|  | $c | Dimensões | Sim | Dimensões do exemplar | LEXEMPLAR.COMPRIMENTO, LEXEMPLAR.LARGURA, LEXEMPLAR.ALTURA | O subcampo será repetido para cada dimensão que estiver cadastrada. Se houver material anexo, acrescentar o símbolo + no final da última dimensão |
|  | $e | Material anexo | Não | Material anexo | LEXEMPLAR.MATERIALANEXO | Se houver material adicional cadastrado para o exemplar (anexo material adicional), exibir o nome do tipo de publicação, com a quantidade. Exemplo: 1 CD-ROM + 2 mapas. Este tipo de material prevalece sobre o campo material anexo do cadastro de exemplar |
| 310 | $a | Periodicidade atual da publicação | Não | Periodicidade da publicação | LPERIODICIDADE.PERIODICIDADE |  |
| 326 | $a | Data de publicação e/ou designação sequencial | Não | Volume, número do exemplar (mês e ano) | LVOLUME.DESCVOL, LEXEMPLAR.NEXEMPPER (LEXEMPLAR.MES, LEXEMPLAR.ANO |  |
| 440 | $a | Título da série | Não | Nome da série | LCOLECAOSERIE.COLECAO OU LCOLECAOSERIE.SERIE | Como o cadastro do sistema suporta a inserção de dois campos distintos, para geração do marc dar-se-á preferencia para a coleção cadastrada e se não houver, a série. |
|  | $v | Número do volume | Não | Volume da série | LPUBLIC.DESCVOLCOLSER |  |
| 500 | $a | Nota geral | Não | Notas gerais da publicação | LPUBLIC.IDMEMOGERAIS -> LMEMO.VALMEMO |  |
| 502 | $a | Nota de dissertação ou tese | Não | Notas de dissertação da publicação | LPUBLIC.IDMEMODISSERTACAO -> LMEMO.VALMEMO |  |
| 504 | $a | Nota de bibliografia | Não | Notas bibliográficas da publicação | LPUBLIC.IDMEMOBIBLIOGRAFICAS -> LMEMO.VALMEMO |  |
| 505 | $a | Nota de conteúdo | Não | Notas de conteúdo da publicação | LPUBLIC.IDMEMOCONTEUDO -> LMEMO.VALMEMO |  |
| 520 | $a | Resumo | Não | Resumo/Observação | LPUBLIC.IDMEMORESOBS -> LMEMO.VALMEMO |  |
| 650 | $a | Assunto | Não | Assunto da publicação | LASSUNTO.ASSUNTO |  |
| 700 | $a | Sobrenome ou prenome do autor | Não | Nome do autor normalizado | LAUTOR.NOME | Somente autores cuja função não seja de autor principal (pessoal) |
|  | $d | Datas associadas ao nome | Não | Ano de nascimento - Ano de morte | LAUTOR.ANONASC - LAUTOR.ANOFAL |  |
|  | $e | Relação com o documento | Sim | Sigla da função do autor | LAUTORFUNC.SIGLA |  |
| 710 | $a | Nome da entidade ou lugar | Não | Nome do autor entidade | LAUTOR.NOME | Somente autores cuja função não seja de autor principal (institucional) |
| 856 | $u | Caminho do arquivo (URI) | Sim | Caminho do arquivo digital | LPUBLIC.PATHARQ |  |
