---
content_hash: 786ef7075ea09797b3f0791bcaa427f7bbf6b15b778a5fa05021519b97175c4e
fetched_at: '2026-06-29T00:10:22.668197+00:00'
page_id: '498696745'
product: rm
source: tdn-rm
title: Anexo eSocial
type: documentation
url: https://tdn.totvs.com/display/LRM/Anexo+eSocial
version: 6
---

---

**Objetivo**

O anexo eSocial existente no cadastro do Cliente/Fornecedor foi implementado pelo produto TOTVS Folha de Pagamento e tem como objetivo parametrizar informações a serem levadas para o eSocial.

---

Para o preenchimento do grupo **S-1005 - Informações de Estabelecimentos/Obras**, é necessário que o campo "Tipo da Lotação", existente no menu eSocial | Lotação Tributária, seja igual a "01-Classificação da atividade econômica exercida pela Pessoa Jurídica para fins de atribuição de código FPAS, inclusive obras de construção civil própria".

**Considera dados da Filial**

Ao selecionar este parâmetro, as informações da filial indicada serão consideradas no processamento.

Caso o parâmetro esteja desmarcado, os campos **CNAE**, **RAT**, **FAP** e **Registro de Ponto** serão habilitados e deverão ser preenchidos.

**FAP**

Ao marcar os parâmetros **"Tomador de serviço folha"** e **"Obra Própria"**, os campos do FAP serão habilitados. Quando preenchidos, o XML do evento S-1005 considerará essas informações para o preenchimento da tag referente ao processo FAP.

**ATENÇÃO:**

* + Quando um tomador possuir múltiplos CEIs, será gerado um gatilho para o tomador e outro para cada**CEI**. O XML do evento S-1005 considerará as informações do FAP registradas no respectivo CEI.
  + Caso não deseje que o sistema busque os dados do processo do FAP no Cliente/Fornecedor, marque o parâmetro **"Considera Dados da Filial"**. Com essa opção ativada, os dados serão obtidos a partir da filial informada nesse parâmetro.

Maiores informações acesse o link  [DT-S1005:Tratar a geração do grupo <procAdmJudFap> para obra própria (CNO/CEI)](https://tdn.totvs.com/pages/viewpage.action?pageId=929925143)

**Tipo de Controle de Ponto**

**Indicativo de Substituição da Contribuição Patronal da Obra de Construção Civil**

Para habilitar este campo, é necessário que no menu eSocial | Informações do Empregadorno campo "Indicativo de Construtora" esteja definido como **"1-Empresa Construtora"** .
