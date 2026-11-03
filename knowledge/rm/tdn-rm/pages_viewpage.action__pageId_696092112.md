---
content_hash: 3c42aac0f3d0a6da833357c5975112fd33e665349ee8fc54969bdea56bb6a807
fetched_at: '2026-06-29T00:11:21.436845+00:00'
page_id: '696092112'
product: rm
source: tdn-rm
title: Informações Fiscais Adicionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=696092112
version: 13
---

#f5f5f5#363636noneINFORMAÇÕES FISCAIS ADICIONAIS 

## **Conteúdo**



## **01. Visão GeralVisaoGeral**

O cadastro dos campos livres permite acrescentar e personalizar os registros "0450: Tabela de informação complementar do documento fiscal" e "0460: Tabela de observações do lançamento fiscal" na geração da EFD ICMS IPI. Este cadastro é feito por Coligada, e seus registros cadastrados podem ser ativados e desativados conforme necessidade.

## **02. Informações Fiscais AdicionaisCadastro**

O submenu pode ser acessado através do Módulo Gestão Fiscal | Cadastros | Na divisão de "Globais" opção Mais | Informações Fiscais Adicionais

Imagem

É necessário conceder permissão no perfil do usuário para acesso ao menu.

Nela, é possível salvar os campos de Registro, Código, Descrição para realizar a integração com os campos livres da NFE para geração do SPED.

Imagem

**Campos**

* **Registro:** Se o cadastro é para o registro 0450 ou 0460
* **Código**: Até 6 dígitos
* **Descrição**: Até 255 dígitos
* **Ativo**: deverá ser definido se este campo está ativo para uso

Alterar código ou descrição dos registros

É possível alterar o código ou a descrição de um registro já existente, porém, essa alteração também pode refletir no SPED Fiscal. Caso este não seja o comportamento desejado, o ideal é que um novo registro seja cadastrado.

## **03. Outras informaçõesOutrasInformacoes**

Disponível a partir da versão 12.1.33.  
Patches:  12.1.33.280 | 12.1.34.183 | 12.1.2205.122

Mediante a atualização da Base de Dados (script LI.2022.06\_03).

Mais informações em [Atualização da Base de Dados RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000994448-Framework-Framework-RM-BD-Como-converter-atualizar-a-Base-de-Dados-RM)

#f5f5f5#feac0eDocumentos Relacionados10%90%10%90%

**[Geração dos Campos Livres NF-e](https://tdn.totvs.com/pages/viewpage.action?pageId=422545956)**

10%90%

**[Campos de Uso Livre (Nota Fiscal Eletrônica)](https://tdn.totvs.com/pages/viewpage.action?pageId=687748443)**

10%90%

**[Grupos V, VA, W, W01, W02, X, Y, YA, YB (Informações Adicionais do Item, Totalizadores, Cobrança e Pagamento, Intermediador)](https://tdn.totvs.com/pages/viewpage.action?pageId=448601189)**

10%90%

**[Grupos Z, ZA, ZB, ZC, ZD, ZX e ZZ (Informações Adicionais da NF-e)](https://tdn.totvs.com/pages/viewpage.action?pageId=538499185)**

10%90%10%90%

**[SPED](https://tdn.totvs.com/pages/viewpage.action?pageId=504818346)**
