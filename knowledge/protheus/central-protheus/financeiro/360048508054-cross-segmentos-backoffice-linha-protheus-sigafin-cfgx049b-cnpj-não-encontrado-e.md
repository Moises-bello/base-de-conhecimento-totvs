---
article_id: 360048508054
category: Financeiro
content_hash: fc82ccb0d9b11c98330313480cd28a998720ff64a2621d923dfa6292d51ad721
fetched_at: '2026-06-28T22:38:01.229415+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CFGX049B  - CNPJ não
  encontrado em nossos servidores ou não é valido e /ou não tem acesso aos nossos
  serviços de hardlock
type: support-article
updated_at: '2026-01-20T17:23:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048508054-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CFGX049B-CNPJ-n%C3%A3o-encontrado-em-nossos-servidores-ou-n%C3%A3o-%C3%A9-valido-e-ou-n%C3%A3o-tem-acesso-aos-nossos-servi%C3%A7os-de-hardlock
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26104533408535)***Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao tentar utilizar o **CNAB Cloud** (**CFGX049B**), para uma filial em especifico, é retornada a mensagem:

**VALIDAÇÃO DE ACESSO AO SERVIDOR DE ARQUIVOS TOTVS**

"CNPJ não encontrado em nossos servidores"

"CNPJ não é valido e /ou não tem acesso aos nossos serviços de hardlock"

![](https://p23.zdusercontent.com/attachment/888110/UnotsKxuC5AqbdjoO1Sikw1Tv?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..aoY3lDtkmBV9adsSLEojpg.eUT6PJBqhTOKB6i_R5Lt5Uw-y7vm27Ch2vBdBQ-CLnBuxZJKWfvhu1qprTvP41QnSSTodxdsZ_TnjFfps77UvUDLTasUuZUNy4_bBInJ8vVsXBt1qzk8DoCe4i9BhRVFH0RKPxJuA-72JlWhRW1xmCFGphgobzGuSvukX1ehAibDaz9mbhngREkBNXDxigXM89teLvOJHm4b5EM61tuJkRVzAUcK8nNhi29cd2rgG7-3WrHy0Mz9Wxt2j8vZ8d37qy27Q37n4elJisA2nQp_iCIuADJqcus29v3OMGJxeM0.m0Razk0YLyAMppJGwcM_Pg)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Causa**CNPJ não consta no cadastro de empresas no módulo Configurador.  
  
**Solução**-Acessar o módulo **Configurador**  
-Clicar em **Ambiente**/**Empresas**/**Filial**-Inserir o CNPJ na filial que não esteja.

![CNAB_Cloud.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360073276973)

**📢️ Importante:**

O **CNPJ utilizado para validação no Wizard de download dos layouts CNAB** deve ser o **CNPJ principal cadastrado junto à TOTVS**, ou seja, o **CNPJ vinculado ao registro do cliente no Suporte TOTVS**.

Como cada cliente possui **apenas um CNPJ cadastrado no suporte**, o download dos layouts só será permitido para esse CNPJ principal.

Caso seja necessário utilizar os **layouts CNAB em outras empresas com CNPJs diferentes**, basta:

1. **Realizar o download dos layouts** utilizando o CNPJ cadastrado no suporte;
2. **Copiar os arquivos de layout** para as demais empresas que utilizam CNPJs distintos

 - Caso o CNPJ esteja correto, verificar se possui regra do firewall para o endereço/porta abaixo

<http://wshlcloud.totvs.com.br:8081>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26104936025623)

**Saiba Mais:**  
[Criação de Empresas e Filiais](https://tdn.totvs.com/pages/viewpage.action?pageId=271174732)  
[CNAB Cloud - Financeiro](https://tdn.totvs.com/display/public/PROT/CNAB+Cloud+-+Financeiro)  
[CFGX049B - Instalar o CNAB Cloud e Usabilidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048501574-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CFGX049B-Instalar-o-CNAB-Cloud-e-Usabilidade)
