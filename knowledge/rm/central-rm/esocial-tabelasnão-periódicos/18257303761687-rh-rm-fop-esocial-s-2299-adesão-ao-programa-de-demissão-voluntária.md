---
article_id: 18257303761687
category: eSocial - Tabelas/Não Periódicos
content_hash: ee65e8f189c5caed771fcc64dff41c21774d267c93ca049097a503d5983f13b1
fetched_at: '2026-06-28T22:47:10.513819+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - S-2299: Adesão ao Programa de Demissão Voluntária'
type: support-article
updated_at: '2026-06-15T13:07:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18257303761687-RH-RM-FOP-eSocial-S-2299-Ades%C3%A3o-ao-Programa-de-Demiss%C3%A3o-Volunt%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18257288845207)  Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como cadastrar uma rescisão e gerar um XML S-2299 para casos em que o funcionário possui Adesão ao Programa de Demissão voluntária?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões

                                                 

**Solução**  
Conforme leiaute do eSocial, o indicativo de desligamento que ocorreu por meio de adesão a programa de demissão voluntária (PDV) deverá ser indicado através da *tag* **indPDV** do S-2299.

*Leiaute S-1.2 - S-2299*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18256109894679)

Para este indicativo, foi criado o parâmetro **Tem Adesão ao Programa de Demissão Voluntária** no cadastro da rescisão do funcionário. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18256363578647)

A *tag* **indPDV** só deve ser informada se o motivo de desligamento for **diferente** de {10, 11, 12, 13, 28, 29, 30, 34, 36, 37, 40, 43, 44}, conforme **Tabela 19 - Motivos de Desligamento** do leiaute eSocial. Sendo assim, o parâmetro **não será habilitado** caso seja informado um **tipo de rescisão** igual a **8** (Falecimento), **F** (Falecimento p/ acidente de trabalho), **P** (Falecimento p/ doença profissional), **5** (Transferência sem ônus p/ Cedente) ou **M** (Mudança de Regime Trabalhista). Também não será exibido caso seja informado um tipo de rescisão para o qual exista um **De/Para de desligamento** cadastrado no parametrizador do eSocial, vinculado a um dos motivos de desligamentos supracitados.  
  
**Importante**  
Como a *tag* só existe à partir do Leiaute S-1.2, ela não será gerada em leiautes anteriores ainda que esteja marcada no cadastro de rescisão do funcionário.  
  
**Saiba mais**  
Para mais informações, acesse:

* [Alterações - S-2299 - S-1.2](https://tdn.totvs.com/pages/viewpage.action?pageId=789389052)
