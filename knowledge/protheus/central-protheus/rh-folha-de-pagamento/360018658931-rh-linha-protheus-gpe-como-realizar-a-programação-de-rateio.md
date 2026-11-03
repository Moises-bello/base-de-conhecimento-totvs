---
article_id: 360018658931
category: RH - Folha de Pagamento
content_hash: 88483858c54bf55bf414f66beec60116268cc8a9a6bd6dddda4ed849e8efe3d7
fetched_at: '2026-06-28T22:44:14.734619+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar a programação de rateio
type: support-article
updated_at: '2026-02-09T18:30:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018658931-RH-Linha-Protheus-GPE-Como-realizar-a-programa%C3%A7%C3%A3o-de-rateio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31586338965143)Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como parametrizar o sistema para que as **verbas de folha de pagamento sejam rateadas por centro de custo**, utilizando a programação de rateio?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Verifique o parâmetro **MV\_RATPROV**, que permite o rateio das verbas na Folha e na Provisão.  
**SIGACFG** em **Ambiente > Cadastros > Parâmetros (CFGX017)**;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014065371)  
  
Se o **conteúdo** do parâmetro estiver com **S**, o sistema utilizará o rateio no cálculo da provisão e da folha.  
  
2. No cadastro de verbas, em **Atualizações > Definições de Cálculos > Verbas (GPEA040)** no campo **RV\_ENCARCC** da aba **Contabilização** informar a opção **B** apenas para a verba de salário e as demais, deverão estar como **S**ou**N** (caso não queira efetuar o rateio).

**- B** para as verbas que formarão a base da divisão para rateio de centro de custo.  
**- S** para as verbas que serão rateadas por centro de custo.  
**- N** para as verbas que não serão rateadas por centro de custo.  
  
No exemplo abaixo, utilizei a verba de salário ID 0031.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014065491)  
  
3. Para que **verbas de origem I e origem G**, para que sejam rateadas deve-se habilitar o **mnemônico P\_LRATINFO = .T.** em **Atualizações > Definições de Cálculos > Mnemônicos (GPEA300)**, dessa maneira verbas de plano de saúde por exemplo, serão rateadas. Desde que no cadastro de verbas também estejam **configuradas para rateio**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014065571)  
  
4. Realize a **programação de rateio**, através da rotina em **Atualizações > Funcionários > Programação de rateio** (**GPEA056)**. Informando Mês/Ano de inicio e término, centro de custo e percentual de rateio. Lembrando que o percentual sempre deve **totalizar 100%**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014065751)  
  
Para que as colunas **Item Contábil e Classe Valor** sejam apresentadas na tela de rateio, o cliente deverá estar com o **MV\_ITMCLVL** habilitado, esta funcionalidade permitirá ao cliente efetuar o rateio por item e classe de valor. Para habilitar o parâmetro acesse o **Configurador SIGACFG** em **Ambiente > Cadastros > Parâmetros (CFGX017)**;  
  
5. **Calcule** a folha de pagamento. Caso tenha verbas de plano de saúde ou outros benefícios, é necessário calcular o beneficio e **realizar a integração para folha de pagamento**.  
Após integração, calcular o roteiro FOL.  
  
6. Verifique que as verbas foram rateadas na consulta por funcionário.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014066031)  
  
**Saiba Mais**  
Acesse o *link* a seguir para verificar o parâmetro referente **ao rateio no eSocial:** <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057926754>
