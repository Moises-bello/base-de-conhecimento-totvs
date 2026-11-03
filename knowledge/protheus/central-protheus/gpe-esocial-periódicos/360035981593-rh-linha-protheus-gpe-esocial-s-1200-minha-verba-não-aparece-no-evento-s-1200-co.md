---
article_id: 360035981593
category: GPE - eSocial - Periódicos
content_hash: f6f8005e42a6da2f9afe8210b095319862c88a256e46d63f7963bc7a38c0dcf4
fetched_at: '2026-06-28T22:45:07.510044+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial  - S-1200 - Minha verba não aparece no
  evento S-1200, como saber se ela está configurada no Protheus como verba de diferença
  de Dissidio
type: support-article
updated_at: '2025-07-22T12:59:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035981593-RH-Linha-Protheus-GPE-eSocial-S-1200-Minha-verba-n%C3%A3o-aparece-no-evento-S-1200-como-saber-se-ela-est%C3%A1-configurada-no-Protheus-como-verba-de-diferen%C3%A7a-de-Dissidio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27255036914967)** Tempo aproximado para leitura: **00:02:00min****Dúvida**S-1200 - Minha verba X não aparece no evento S-1200, como saber se ela está configurada no Protheus como verba de diferença de Dissidio?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
 **Solução**  
As verbas da folha de pagamento não são enviadas ao **TAF** na coluna de pagamento mensal quando essa verba está informada no campo "**Verba de Dissidio (RV\_CODCOM\_)**" do **cadastro de verbas (SRV)** do **GPE** para outra verba.

**Exemplo:** Ao gerar o evento S-1200 verifiquei que minha Verba de código "**100 - Salario**" existe no cálculo da Folha de Pagamento do Trabalhador no GPE, porém ela não é levada ao TAF após a integração dos eventos periódicos.  
  
Esse erro vai ocorrer porque a verba de código "**100 - Salario**" está informada no campo **Verbas para Dissidio** (RV\_CODCOM) de uma outro verba. Por exemplo verba "**103 - Dif. de Salario**", desta forma a verba "**100 - Salario**" NÃO era enviada no evento S-1200.  
  
O campo **Verbas para Dissidio** (RV\_CODCOM) deve conter apenas códigos de verbas que são utilizados para gerar o valor de diferença de dissidio a ser pago. Não deve existir nesse campo código de verbas utilizados no calculo da folha.  
  
Para analise siga as orientações abaixo:  
1. Para saber qual verba está incorreta gere o relatório do evento S-1200 filtrando o CPF do trabalhador com erro. Em caso de dúvidas consulte: [RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no módulo GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE)  
  
2. Após gerar o relatório em excel, siga para a aba "**Inconsistências**" do relatório. E se encontrar a **mensagem**: "Verba**X** despreza do grupo **infoPerApur** (Remuneração no período de apuração) pois esta cadastrada no campo Verba P. Diss (RV\_CODCOM) da verba**Y**. Dessa forma, a diferença de dissidio será gerado no grupo **infoPerAnt** (Remuneração em Períodos Anteriores)".   
  
**Efetue a seguinte orientação:**  
Acesse no cadastro de verbas a verba "**Y**", e na aba Dissidio apague ou altere para uma verba correta o campo **Verbas para Dissidio** (RV\_CODCOM) que vai estar com o código da verba "**X**" mencionada no relatório de inconsistência.

**Exemplo:**Inconsistência apresentada no [relatório de conferência do evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33632604375831)  
Verba 160 desprezada do grupo infoperApur (Remuneração no período de apuração) pois está cadastrada no campo Verba P.Diss (RV CODCOM) da verba 075. Dessa forma, a diferença de dissidio será gerada no grupo infoPerAnt (Remuneração em Periodos Anteriores)  
O ajuste necessário nesse caso é acessar o cadastro da verba **075**, na aba Dissidio Retroativo, retirar a verba código da **160** do campo **Verbas para Dissidio**, ou alterar para uma verba correta conforme [Manual do Dissidio Retroativo](https://tdn.totvs.com/pages/releaseview.action?pageId=220889925).

**Importante**

* Observar que no campo **"Verba de Dissidio (RV\_CODCOM)"** só podem ser informadas verbas específicas para pagamento de diferença de dissidio.
* Para mais informação relacionadas a configuração do Reajuste Retroativo/Dissídio no módulo **GPE**acesse a página do **[MANUAL GPE - Dissídio Retroativo](http://tdn.totvs.com/pages/releaseview.action?pageId=220889925)**.
* Após ajustes deve ser gerado novamente o evento S-1200.

**Saiba Mais**Para saber mais consulte os links abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-1200 - Quais verbas serão enviadas para o eSocial nos casos de Dissidio Retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018355852-RH-Linha-Protheus-GPE-eSocial-S-1200-Quais-verbas-ser%C3%A3o-enviadas-para-o-eSocial-nos-casos-de-Dissidio-Retroativo)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
