---
article_id: 20643207854743
category: eSocial - Gerar XML/ Integração Evento
content_hash: 7795eb590c8ebb2fdf406e98145955f1e40b8d02594e0a8c1f183c919bc252af
fetched_at: '2026-06-28T22:47:12.015598+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Como enviar a correção de INSS para funcionários
  demitidos que já possuem S-2299 no governo, após a atualização da tabela INSS 2024
type: support-article
updated_at: '2024-06-24T17:29:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20643207854743-RH-RM-FOP-eSocial-Como-enviar-a-corre%C3%A7%C3%A3o-de-INSS-para-funcion%C3%A1rios-demitidos-que-j%C3%A1-possuem-S-2299-no-governo-ap%C3%B3s-a-atualiza%C3%A7%C3%A3o-da-tabela-INSS-2024
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20643207841687) Tempo aproximado para leitura: 00:02:30 min **Dúvida**Como enviar a correção de INSS para funcionários demitidos que já possuem S-2299 no governo, após a atualização da tabela INSS 2024?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**

Foi publicada a Portaria Interministerial MPS/MF nº 2, de 11 de janeiro de 2024, do Ministério da Previdência Social e do Ministério da Fazenda, que divulga a tabela de faixas para atribuição de alíquotas previdenciárias, bem como limite de salários de contribuição ao INSS, além de reajustar os benefícios pagos pelo Instituto Nacional do Seguro Social (INSS) e os demais valores constantes do Regulamento da Previdência Social (RPS).

A cota de salário-família passou a ter o valor de R$ 62,04, sendo paga aos segurados com remuneração mensal não superior a R$ 1.819,26. Mais informações acesse: [Liberado o envio de eventos de folha para o eSocial após publicação de portaria que reajusta valores previdenciários em 2024](https://www.gov.br/esocial/pt-br/noticias/liberado-o-envio-de-eventos-de-folha-para-o-esocial-apos-publicacao-de-portaria-que-reajusta-valores-previdenciarios-em-2024)

Para tratativa no sistema RM, será necessário retificar o evento S-2299 da rescisão. Para isso, será necessário seguir o passo a passo abaixo:

1. Acesse **eSocial | Fila de Eventos Não Periódicos**;

2. Identifique e selecione o evento S-2299 desejado, acesse **Processos | Gerar Retificação Arquivo eSocial**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20646259537431)

3. Para empresas que trabalham com tomador de serviços, faz-se necessário distribuir Sefip antes de gerar o XML de retificação do S-2299. Acesse **Encargos | Sefip | Distribuir Sefip** e distribua Sefip para o  funcionário desejado. Caso a competência da rescisão já esteja fechada, faz-se necessário marcar **Sobrepor dados existentes**.

4. Gere o XML S-2299 de retificação e integre com o governo.

**Importante**

A transmissão dos eventos de Desligamento (S-2299) e Término do Trabalhador Sem Vínculo de Emprego (S-2399) não foi bloqueada. Como a portaria com as novas alíquotas foi publicada com vigência retroativa a 01/01/2024, cabe ao empregador realizar, antes do fechamento da folha do mês de janeiro/2024, a retificação dos eventos que foram transmitidos antes da implantação da alteração, para que os cálculos passem a contemplar os valores atualizados pela portaria.
