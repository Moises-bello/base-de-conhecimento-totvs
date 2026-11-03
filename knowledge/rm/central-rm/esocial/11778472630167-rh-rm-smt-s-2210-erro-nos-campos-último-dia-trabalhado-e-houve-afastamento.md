---
article_id: 11778472630167
category: eSocial
content_hash: 2555b5cb15635afa96a25829fecbf77cea183e861cf777c9c9b9c8137c80cd3a
fetched_at: '2026-06-28T22:47:39.074948+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - S-2210: Erro nos campos Último Dia Trabalhado e Houve Afastamento'
type: support-article
updated_at: '2026-06-02T14:55:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11778472630167-RH-RM-SMT-S-2210-Erro-nos-campos-%C3%9Altimo-Dia-Trabalhado-e-Houve-Afastamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16034516370199) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao enviar o evento o evento S-2210 ao governo é retornado os erros abaixo, o que fazer?  
  
*Código da Resposta: 401 - Conteudo do evento invalido*  
*Sequência: 000001 - Tipo: Erro - Codigo da Ocorrência: 1 - Descrição : Campo de preenchimento obrigatorio: Ultimo Dia Trabalhado. - Localização: /Social/evtCAT/cat/ultDiaTrab*

*Sequência: 000002 - Tipo: Erro - Codigo da Ocorrência: 1 - Descrição: Campo de preenchimento obrigatorio: Houve Afastamento. - Localização: /eSocial/evtCAT/cat/houveAfast*  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11778210582935)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - **12.1.34.221**, **12.1.2205.161** **12.1.2209.106** e **superiores.**  
  
**Solução**Os campos **ultDiaTrab** e **houveAfast** deverão obrigatoriamente ser preenchidos para as CAT's em que a  data do acidente seja igual ou superior ao dia **16/01/2023**.

A nova regra em questão decorreu a partir da Nota Técnica 06/2022 do eSocial a qual traz melhorias ao layout 1.0.   
  
Para maiores informações sobre a NT acesse: [RH - RM - SMT - Ajustes realizados nos eventos de SST/eSocial referente a Nota Técnica nº 06/2022](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11750964423447)  
  
Para correção do erro no evento, realize as seguintes validações:  
  
1 - Avalie se o RM está atualizado para umas das versões 12.1.34.221, 12.1.2205.161 12.1.2209.106 ou superiores.  
  
2 - E se os scripts do RM Atualizador foram executados. Segue orientações para validar na documentação a seguir:

[Framework - Framework RM - BD - Scripts Opcionais/Intermediários RM.Atualizador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007553911)  
  
3- No RM os dados referente a parametrização poderão ser validados no modulo da Folha de Pagamento no menu **Condigurações** | **Parametrizador** ao abrir o assistente clique em avançar, selecione o processo  **eSocial** e avance até a etapa **Configurações gerais 1/7**. No campo **Versão do Leiaute** selecione a versão do layout vigente para que os XMLs gerados no RM estejam de acordo com a Nota Técnica.  

4 - Na CAT criada os campos **'Último dia trabalhado'** e **'Houve afastamento'** deverão estar preenchidos. Lembrando que o cadastro da CAT fica disponível no modulo de **Segurança e Saúde Ocupacional** menu **CAT/Incidentes | Ocorrências Acidente de Trabalho**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34092728313239)  
  
5 - Caso ainda mesmo após criação dos campos no XML este ainda seja rejeitado, gentileza entrar em conta com a equipe **TAF eSocial Segregado** para que possam ser orientados em relação aos ajustes de Notas Técnicas e/ou Layout no ambiente **TAF/TSS**. *A equipe poderá ser acionada através do telefone (11) 4003 0015 >> URA 2-2-2-3-6-3 ou via chat.*  
  
  
**Saiba Mais:**

Para maiores informações, acesse:

[- Leiaute Versão S-1.1](https://tdn.totvs.com/pages/viewpage.action?pageId=702365686#1-1)
