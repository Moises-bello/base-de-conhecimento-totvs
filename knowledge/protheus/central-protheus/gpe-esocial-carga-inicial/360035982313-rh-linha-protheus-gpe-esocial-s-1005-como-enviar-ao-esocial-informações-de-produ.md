---
article_id: 360035982313
category: GPE - eSocial - Carga Inicial
content_hash: 9f14d5f66eeac4122ea6954ee71ddc6f8f3536ae9526958b9d925b99ce7d67f3
fetched_at: '2026-06-28T22:45:03.177812+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1005 - Como enviar ao eSocial informações
  de Produtor Rural (CAEPF)
type: support-article
updated_at: '2023-10-17T18:51:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035982313-RH-Linha-Protheus-GPE-eSocial-S-1005-Como-enviar-ao-eSocial-informa%C3%A7%C3%B5es-de-Produtor-Rural-CAEPF
---

**Dúvida**Como enviar ao eSocial informações de Produtor Rural (**CAEPF**)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**No Manual de Orientação do eSocial (MOS) diz que o CAEPF deve ser cadastrado por estabelecimento, conforme demostrado abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18337793783447)  
  
Para que seja realizado o cadastro da empresa e estabelecimento, de forma que atenda o leiaute do eSocial, é necessário seguir essas premissas de cadastros:

* A filial deve estar cadastrada dentro do Configurador com o Tipo de Inscrição como "3 - CPF" ou Tipo de Inscrição como "1 - CEI" e Produtor Rural como "1 - Pessoa Física";
* Realizar o cadastro da filial dentro do Cadastro de Complemento de Estabelecimentos - Rotina FISA137 (Programa: FISA137.PRW / Tabela: F0F) e informar o Número do CAEPF e o Tipo CAEPF igual a "2";
* Realize a carga inicial do evento S-1005.

Para entender os ajustes realizados no SIGAGPE para atender a demanda do Produtor Rural (CAEPF) e o envio dos eventos ao eSocial **[clique aqui para visualizar o Boletim Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=327334568)**.

**Passo a passo:**

**1º Passo:**  
Quando você administra esse CAEPF em seu ambiente do Protheus, ele é considerado uma Empresa e terá o seu próprio evento **S-1000**, para isso você deverá cadastrá-lo no seu SIGAMAT.  
O cadastro da filial deve estar com o Tipo de Inscrição como "3 - CPF" ou Tipo de Inscrição como "1 - CEI" e Produtor Rural como "1 - Pessoa Física" Para mais informações acesse: [Como criar empresas e/ou filiais no Protheus](https://tdn.totvs.com/x/TMwpE)  
  
Caminho do SIGACFG: Ambiente> Empresas> Filial  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18339266446871)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18339175347607)  
  
**2º Passo:**  
Para correta geração do evento S-1005 quando se tratar de um CAEPF, é necessário realizar o cadastro da filial dentro do Cadastro de Complemento de Estabelecimentos (Rotina FISA137) e informando o Número do CAEPF e o Tipo CAEPF igual a 2.  
  
Caminho: Buscar a rotina na pesquisa:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18339667955607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18256157433879)  
  
**3º passo:**  
Integrar pela Carga Inicial o S-1005 dos estabelecimentos cadastrados.   
  
Caminho do GPE: Miscelânea> Esocial> Carga Inicial  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18340426262423)  
XML S-1005 gerado com Tipo de Inscrição igual a 3 (CAEPF) e numero de inscrição com o CAEPF:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18341143395863)  
  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Artigos S-1005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050822873)[Artigos S-1020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051258534)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
