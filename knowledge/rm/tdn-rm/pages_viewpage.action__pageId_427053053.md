---
content_hash: 0d30029be3629e87562ea30cf44be756e65024d6bb4dbb46dfeca7c518b3af2c
fetched_at: '2026-06-29T00:09:38.645152+00:00'
page_id: '427053053'
product: rm
source: tdn-rm
title: Código de Ajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=427053053
version: 32
---

# 1. Introdução

Este cadastro possibilita ao usuário parametrizar os códigos de ajustes *default* que afetam suas operações por estado, diretamente no TOTVS Gestão Fiscal.

# 2. Como habilitar

Para habilitar o novo menu, acesse: Serviços Globais | Segurança | Perfil.

Na tela de Edição de perfil do TOTVS Gestão Fiscal clicar na aba "Acesso a Menus" e selecionar a permissão em Gestão Fiscal | Cadastros | Específicos | Mais... | [01.01.10.18] Código de Ajuste

# 3. Cadastro

Para o cadastro do código de ajuste localize o menu Cadastros | Específicos | Mais... | Código de Ajuste.

Na visão, clique no botão "Novo" para criação do cadastro. Os campos presentes neste cadastro são:

* UF
* Registro. Com as opções:

  + C197/D197/C597
  + C177
  + E115
  + 1921
  + C181
  + C185
  + C186
* Código de Ajuste: Esse campo é utilizado para todos os registros e devem ser preenchidos de acordo com as tabelas disponibilizadas pela Receita Federal.
* Tipo de Crédito: Esse campo será apresentado apenas se informado o valor E115 no campo de registro. Nesse campo o usuário poderá selecionar uma das opções abaixo, que será utilizado na geração das tags **cBenef**,**cCredPresumido** (gCred) e **cBenefRBC**, da **NF-e**:  
    
  Para mais informações do grupo **gCred** verifique o **Grupo I05g -** **Grupo Credito Presumido** na nossa [documentação](https://tdn.totvs.com/pages/viewpage.action?pageId=953002044).  
    
  + Não se Aplica
  + Credito presumido
  + Redução de BC - Diferido
* Cadastro de Código de Ajuste

Gestão Fiscal | Cadastros | Mais

* Descrição complementar do ajuste: Possui tamanho máximo de 255 caracteres.
* Aplicar em, contendo as seguintes opções:

+ No Lançamento Fiscal (não permitido marcar para os registros C177, C181, C185 e C186)
+ No Item (não permitido marcar para o Registro E115, exceto quando o código de ajuste é iniciado em SC85”)

* Base de cálculo – lookup para o Cadastro de Fórmulas. Será apresentado quando for selecionada a opção “C197/D197/C597/1921”.
* Alíquota – lookup para o Cadastro de Fórmulas. Será apresentado quando for selecionada a opção “C197/D197/C597/1921" ou E115”.
* Valor do ICMS/ICMSST – lookup para o Cadastro de Fórmulas. Será apresentado quando for selecionada a opção “C197/D197/C597/1921”.
* Fórmula de Outros Valores – lookup para o Cadastro de Fórmulas. Será apresentado quando for selecionada a opção “C197/D197/C597/1921”.
* Cadastro de Processos Judiciais - lookup para o Cadastro de Processos Judiciais. Será apresentado em quaisquer opções.

Caso seja realizada a inclusão de um registro com os dados de Registro, Aplicar em Estado e Código de Ajuste repetidos será notificado e solicitado ao usuário que confirme a inclusão.

Vídeos How To 4left1Vinculação no CFOPCódigo de Ajuste e vinculação no CFOP

648432
