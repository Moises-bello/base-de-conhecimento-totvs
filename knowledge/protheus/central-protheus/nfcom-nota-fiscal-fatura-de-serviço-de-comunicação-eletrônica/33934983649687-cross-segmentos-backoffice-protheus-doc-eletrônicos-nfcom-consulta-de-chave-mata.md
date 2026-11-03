---
article_id: 33934983649687
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: bfb45a6284de5a8cff7c4c871504d17aed194eee5366ffe1d5d926c39b91fc97
fetched_at: '2026-06-28T22:39:55.121241+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Consulta
  de Chave (MATA103 e SPEDNFE)
type: support-article
updated_at: '2025-12-03T16:49:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33934983649687-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Consulta-de-Chave-MATA103-e-SPEDNFE
---

**Dúvida**  
Como realizar a Consulta de Chave da NFCOM (Nota Fiscal Fatura de Serviço de Comunicação Eletrônico) - Modelo 62?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões      
  
**Solução**  
Atualmente há **duas maneiras** de Consulta de Chave para a NFCOM, sendo elas:   
  
- Via **MATA103** através do campo Chave NFS / Cod. Verificação.  
- Via **SPEDNFE** através do menu Outras Ações -> Consulta Chave;  
  
**Portanto, através da rotina MATA103 (Documentos de Entrada):**  
  
A rotina de Compras (MATA103) utiliza os parâmetros e o certificado do TSS para consultar as chaves. Portanto, é necessário verificar se o certificado da filial que está consultando o documento está válido e se os parâmetros estão devidamente configurados como indicado abaixo:

Acesse a rotina de **Faturamento > Atualizações > Nf-e e Nfs-e > Nf-e Sefaz -> Opção 8-NFCOM:**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33934990065815)**

Dentro da rotina, configure os parâmetros em **Outras ações > Parâmetros NFCom,** exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35970574979351)

É necessário que o TSS esteja atualizado:   
- [Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)  
- [Atualização URL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025394911-TSS-Atualiza%C3%A7%C3%A3o-das-URLs-do-TSS?source=search)  
  
**Para habilitar o campo de chave para espécie NFCOM no documento de entrada:**  
  
Verifique se existe o parâmetro**MV\_CHVESPE** em seu ambiente. Caso sim, informe a espécie NFCOM neste parâmetro.   
  
Caso não existir, você pode cadastrá-lo manualmente:  
Parâmetro: **MV\_CHVESPE**  
Tipo: Caractere  
Cont. Por: (Informar as espécies que devem possuir chave)  
Descrição: Define quais Espécies de Nota Fiscal permite a geração da chave da DANFE.  
  
Se mesmo assim não conseguir consultar a chave, na tabela SPED000 do TSS os parâmetros devem ficar conforme abaixo:

MV\_AMBNFCO=1 (Produção) ou 2 (Homologação)  
MV\_VERNFCO=1.00

**Obs**: Caso não esteja disponível a opção 8-NFCOM, será necessário atualizar a rotina SPEDNFE aplicando o patch abaixo de acordo com sua versão do Protheus:  
**Protheus 12.1.2310:** [Clique aqui para download.](https://suporte.totvs.com/portal/p/10098/download?e=1124963) [SOMENTE GARANTIA ESTENDIDA]  
**Protheus 12.1.2410:** [Clique aqui para download.](https://suporte.totvs.com/portal/p/10098/download?e=1171486)  
  
**Já via SPEDNFE, seguem detalhes abaixo:**  
  
Para realizar a consulta de uma chave de NFCOM via SPEDNFE se faz necessário os seguintes passos detalhados abaixo:  
  
**1.** Acessar a rotina **SPEDNFE** através do Módulo de Faturamento:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33934990061975)  
  
**2.** Ao entrar na rotina, escolher a opção '**8-NFCom**':  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33934990065815)**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33934990068759)**  
  
**3.** Com isso será apresentada a tela abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33934983598231)  
  
**4.** Acessar o menu **Outras Ações -> Consultar Chave:**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33934983600663)**  
  
**5.** Após isso, basta preencher o campo apresentado com a chave desejada:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33934990075927)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33934990079127)
