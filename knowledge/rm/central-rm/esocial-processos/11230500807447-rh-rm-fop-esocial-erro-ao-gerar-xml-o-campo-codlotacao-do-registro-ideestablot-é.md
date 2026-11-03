---
article_id: 11230500807447
category: esocial - Processos
content_hash: 99d74a24fe7d206d8f9e3bcc6ed214309c081e49e73d1b10b0ebf20bbcc1cd9d
fetched_at: '2026-06-28T22:47:08.353356+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: O campo ''codLotacao'' do registro
  ''ideEstabLot'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-12-18T15:57:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11230500807447-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-O-campo-codLotacao-do-registro-ideEstabLot-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24126924649239) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao gerar XML do evento S-1200 ou S-2299 apresenta a mensagem **O campo 'codLotacao' do registro 'ideEstabLot' é obrigatório e não está preenchido.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
O erro ocorre normalmente, quando vincula-se um **Tomador de Serviço** no histórico de Rateio Tomador  para o funcionário e não gerou a Lotação Tributária, referente a este Tomador de Serviço/Seção.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **eSocial | Lotação tributária| Processos** e execute a rotina **Gerar Lotação Tributária;**

![](https://totvssuporte.zendesk.com/attachments/token/ZsLPq5ObAoOGY2MlJdNJJTA72/?name=inline691814333.png)

2. Após, será criado um evento **S-1020** na Fila de Eventos, sendo necessário o envio deste para o ambiente do Governo. Caso não tenha gerado, foi alterado alguma informação no cadastro da Lotação que não se fez necessário a geração do gatilho;  
3. Em seguida gere novamente o evento S-1200 e envie ao eSocial.  
  
**Importante**  
O parâmetro **Utiliza Tomadores de Serviço** fica localizado no menu **Configurações | Parametrizador | Folha Normal | Tomadores de Serviço**. Não é aconselhável marcar ou desmarcar o parâmetro, quando já ocorreram movimentações de Folha e eSocial na coligada, sem consultar um especialista do produto.  
   
**Saiba mais**

Para mais informações acesse:

[- Identificação da origem da Lotação Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015506452-RM-eSocial-Identifica%C3%A7%C3%A3o-da-origem-da-Lota%C3%A7%C3%A3o-Tribut%C3%A1ria?source=search)  
[- Criação das Lotações Tributárias - Como identificar o motivo da criação de cada Lotação Tributária?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015506452-RM-eSocial-Cria%C3%A7%C3%A3o-das-Lota%C3%A7%C3%B5es-Tribut%C3%A1rias-Como-identificar-o-motivo-da-cria%C3%A7%C3%A3o-de-cada-Lota%C3%A7%C3%A3o-Tribut%C3%A1ria-?source=search)  
[- Lotação tributária (S-1020) para empresas que utilizam tomadores de serviços](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015470032-RM-eSocial-Lota%C3%A7%C3%A3o-tribut%C3%A1ria-S-1020-para-empresas-que-utilizam-tomadores-de-servi%C3%A7os?source=search)
