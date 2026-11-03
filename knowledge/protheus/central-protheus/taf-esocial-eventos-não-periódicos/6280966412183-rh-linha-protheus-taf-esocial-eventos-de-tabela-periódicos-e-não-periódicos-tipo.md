---
article_id: 6280966412183
category: TAF - eSocial - Eventos Não Periódicos
content_hash: 9e77d86f7b5552d04c4d83db9a2d72442cd25e9df9b6f38a54ec59764fc55312
fetched_at: '2026-06-28T22:45:17.983433+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos de Tabela, Periódicos e Não
  Periódicos - Tipo: Advertência - Codigo da ocorrência: Descrição: Leiaute do evento
  invalido'
type: support-article
updated_at: '2026-06-25T11:22:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6280966412183-RH-Linha-Protheus-TAF-eSocial-Eventos-de-Tabela-Peri%C3%B3dicos-e-N%C3%A3o-Peri%C3%B3dicos-Tipo-Advert%C3%AAncia-Codigo-da-ocorr%C3%AAncia-Descri%C3%A7%C3%A3o-Leiaute-do-evento-invalido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23702986792087) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No módulo do TAF, ao tentar realizar a transmissão de eventos para o eSocial é apresentada a seguinte rejeição:  
  
**Sequência: 000001 - Tipo: Advertência - Codigo da ocorrência: Descrição: Leiaute do evento invalido**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29715888855447)****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Causa**A partir da data de **02/02/2025**, passa a ser obrigatória a transmissão dos eventos do eSocial no novo **Leiaute S-1.3**. O Governo não aceitará transmissões no antigo **Leiaute S-1.2**.  
  
**Solução**Para solucionar essa ocorrência, será necessário alterar os parâmetros **MV\_VLESOC** e **MV\_TAFVLES** para **S\_01\_03\_00** e atualizar os ambientes com as últimas expedições contínuas:

**1. Alterar os parâmetros:**

Caminho: SIGACFG > Ambiente > Cadastro > Parâmetros:

**MV\_TAFVLES:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29715877375127)

**MV\_VLESOC:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29715877378583)  
  
**2.** Realize a atualização do ambiente com a **Expedição Contínua** mais recente. Para mais detalhes verifique a documentação abaixo:

TAF:

[RH - Linha Protheus - TAF - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)

Protheus RH-eSocial (GPE):

[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)

**Atenção:** Esta atualização possui dicionário de dados, é necessário rodar o UPDDISTR e UPDTAF.  
  
**2.** Atualize também o TSS e Schemas. E para mais detalhes verifique a documentação abaixo:

[TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)  
[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)  
  
**OBSERVAÇÃO:**Se o registro (evento) no TAF, foi integrado em leiaute diferente, será necessário excluir o evento no TAF, e após alterar para o leiaute S-1.3, é necessário integrar o registro novamente do ERP (GPE/RM/Datasul) para o TAF;  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [**TOTVS Informa**](https://informa.totvs.com/)selecione em categorias a área e pesquise por "**Eventos**"  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
