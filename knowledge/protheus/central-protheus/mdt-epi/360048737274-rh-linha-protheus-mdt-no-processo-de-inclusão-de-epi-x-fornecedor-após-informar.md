---
article_id: 360048737274
category: MDT - EPI
content_hash: 4c008bae081d824c2a57943bffe8b6ada770e726f11dcdb2ae1fca2551040759
fetched_at: '2026-06-28T22:44:25.471741+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: 'RH - Linha Protheus - MDT - No processo de inclusão de Epi X Fornecedor, após
  informar o código do produto (Epi) retorna a mensagem: HELP: JAEXISTINF.'
type: support-article
updated_at: '2024-11-05T10:47:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048737274-RH-Linha-Protheus-MDT-No-processo-de-inclus%C3%A3o-de-Epi-X-Fornecedor-ap%C3%B3s-informar-o-c%C3%B3digo-do-produto-Epi-retorna-a-mensagem-HELP-JAEXISTINF
---

**Ocorrência**No processo de inclusão de Epi X Fornecedor, após informar o código do produto (Epi) retorna a mensagem: **HELP: JAEXISTINF**. Problema: Informação já cadastrada. Solução: Verifique o código informado.   
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
**Causa**Ocorre esta mensagem quando já existe o EPI cadastrado contendo o  seu número de C.A. O registro do EPI deve ser único.  
  
**Solução**Cada EPI  **(tabela SB1)** deverá ser único para o seu C.A. Cada EPI deverá ter um cadastro na rotina de Produto (EPI) e assim assimilado ao C.A. gerado pelo sistema CAEPI, na rotina de EPI x Fornecedor.   
De acordo com a publicação do Comunicado 53, no site do ENIT do governo, o que pode ocorrer é a matriz e filial utilizarem o mesmo C.A., conforme consta:  
  
**Art. 11.** Em caso de EPI fabricado pela matriz e/ou suas filiais, o fabricante poderá solicitar a emissão de CA único no CNPJ da matriz, mediante apresentação de relatório de ensaio que elenque todas as unidades fabris do fabricante que produzam aquele equipamento.  
Para tanto, para cada EPI será utilizado apenas um C.A., a fim de garantir que o EPI tenha as especificações descritas no laudo ao qual foi submetido para gerar o C.A.  
  
**Saiba Mais**  
[Artigos sobre Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT)
