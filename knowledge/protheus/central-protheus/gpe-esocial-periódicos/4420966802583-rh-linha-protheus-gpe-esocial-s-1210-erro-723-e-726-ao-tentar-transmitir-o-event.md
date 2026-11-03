---
article_id: 4420966802583
category: GPE - eSocial - Periódicos
content_hash: 916a2f1a8b837a1c66ce5cb8f1a240199d5e4ea4959cb22a195f5b491f9b2960
fetched_at: '2026-06-28T22:45:08.957749+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210 - Erro 723 e 726 ao tentar transmitir
  o evento S-1210 para o eSocial
type: support-article
updated_at: '2025-07-24T20:52:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420966802583-RH-Linha-Protheus-GPE-eSocial-S-1210-Erro-723-e-726-ao-tentar-transmitir-o-evento-S-1210-para-o-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25856900190359) Tempo aproximado para leitura: **05:00:00 min****Ocorrência**Erro 723 e 726 ao tentar transmitir o evento S-1210 para o eSocial

**Tipo: Advertência - Código da Ocorrência: 723** - Descrição : Valor Liquido invalido. O valor esperado do trabalhador CPF: xxxxxxxxxxx e: (xxx,xx).Ação Sugerida: Em caso de pagamento total, o valor liquido deve corresponder ao somatório dos valores de vencimentos e descontos da remuneração e também dos descontos de IRRF e Pensão alimentícia. Em caso de pagamento parcial, o valor liquido deve corresponder ao somatório dos valores de vencimentos e descontos informados no grupo infoPgtoParc.  
  
**Tipo: Erro - Codigo da Ocorrência: 726** - Descrição : Nao foi localizado um evento de rescisao contratual para o trabalhador com mesmo recibo de pagamento.Acao Sugerida:Deve ser um identificador de recibo de pagamento atribuido pela empresa em um dos eventos rescisorios (S-2299 ou S-2399), no campo quot;identificador de recibo de pagamentoquot;..Se Tipo de Pagamento = [2] deve ser um valor atribuido pela empresa em S-2299;.Se Tipo de Pagamento = [3], deve ser um valor atribuido pela empresa em S-2399.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**Quando o governo retorna o erro **723 "Valor Líquido inválido"** atrelado aos erros **726 "Não foi localizado um evento de remuneração"** o problema esta relacionado ao **identificador de pagamento do S-2299** que não foi localizado no site do eSocial.  
  
Todo evento **S-1200** (Remuneração de trabalhador), **S-2299** (Desligamento) e **S-2399** (Desligamento Trabalhador sem Vinculo), tem um **identificador para o demonstrativo de pagamento** denominado no XML com a **tag** ***ideDmDev*** que é a chave do recibo do pagamento apresentado no campo **Iden Dem Pgt/Vl** dentro do **S-1210***.*

Para que o evento **S-1210** (Pagamento Rendimentos) seja aceito pelo *RET* é necessário que exista protocolado no *RET* um evento **S-1200**, **S-2299** ou **S-2399** com mesmo tag/chave *ideDmDev* (**Iden Dem Pgt/Vl**)gerado no **S-1210** referente ao mesmo período de apuração.  
  
Nesse caso sempre que existir no **S-1210 a tag/chave** ***ideDmDev*** (**Iden Dem Pgt/Vl**) ausente ou incorreta vai acontecer esse erro na transmissão.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** **Verifique no TAF** e no governo se foi enviado no **S-2299** o recibo referente a rescisão.  
Consulte o mateiral: [Como consultar no site do eSocial dados do evento S-2299 (Desligamento/Rescisão)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041297433)  
  
**Como verificar no TAF:**  
Acesse no TAF (84) no caminho: atualizações > eventos eSocial > não periodicos > desligamento **(TAFA266)**. Entre no **S-2299** do trabalhador verifique na aba verbas rescisorias se tem na grid com nome **Iden Dem Va** uma linha com o código onde o inicio começa com as letras **RT**.![s-2299_taf.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4420974618007)  
  
**2.** Caso a sua empresa trabalhe com regime de caixa (**se não for caixa pule para o proximo tópico**) verifique também no TAF e no governo se foi enviado no **S-1200** referente ao mês anterior a resicsão o recibo com dados da folha. Ocorre muitos problemas onde o cliente envia para o governo apenas o recibo de adiantamento no **S-1200** ocasionando erro no **S-1210**.  
  
**Como verificar no TAF:**  
**Acesse no TAF (84)** no caminho: atualizações > eventos eSocial > **folha de pagamento** **(TAFA250)**. Entre no **S-1200** do trabalhador no mês anterior a rescisão e verifique na aba Demonstrativos de Valores se tem na grid com nome **Iden Dem Pgt** uma linha com o código onde as 3 ultimas letras são **FOL**.![S-1200_taf.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25856900202775)  
  
Caso exista não a chave com final **FOL** é possivel que não tenha sido enviado para o governo as informações referentes a folha desse trabalhador. Avalie se realmente não foi enviado o pagamento no S-1200 com a chave **FOL** do mês anterior (empresas que trabalham com regime de caixa).  
  
Se o erro estiver no S-1200 do mês anterior a rescisão, ou seja, não tem a informação **FOL** gere novamente o evento S-1200 marcando no GPE a opção "**considerar dados do periodo em aberto**". Para gerar o S-1200 do mês fechado no eSocial será necessario reabrir a folha no governo **(apenas follha eSocial e não folha protheus)** e renviar o evento, pois se não tem o recibo **FOL** no mês anterior, os dados da previdencia para esse trabalhador não foram recolhidos.  
  
Material com orientações:

* [Como retificar eventos S-1200 ou S-1210 que já foram transmitido para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000230862)
* [Como retificar ou reprocessar os Totalizados (DCTFWEB) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025678254)
* [Como consultar no site do eSocial dados do evento S-1200 (Folha de Pagamento)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043290614)

**3.** Verifique se o sistema está atualizado com o ultimo pacote de expedição continua do RH, pois sempre que ocorre erro no fonte relacionado ao evento S-1210 a atualização é gerada no pacote de expedição.  
Link: **[Pacote e Dicionário Correções Expedição Continua RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)**  
  
**Atenção**  
Após atualizar o sistema é necessario **excluir** o S-1210 e gerar novamente, e **retificar** a rescisão **S-2299**.  
Consulte nosso material:  
[S-2299 - Como retificar uma rescisão através do SIGAGPE sem precisar excluir o calculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020865371)  
[S-1210 Como excluir do TAF em lote / massiva os Eventos Periódicos sem protocolo e/ou inconsistentes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035240653)  
  
**4.** Se o erro continuar ocorrendo mesmo após a analise de todos os itens anteriores encaminhe as seguintes informação para analise do suporte técnico.   
  
Encaminhar os dados abaixo de **apenas um trabalhador**:

* Arquivo XML do **GPE e TAF** **S-****1200**mês anterior conforme orientações do artigo:[**S-1200 - Como gerar os arquivos XML do evento S-1200 (Folha de Pagamento) no modulo SIGATAF para análise**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006729801-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-os-arquivos-XML-do-evento-S-1200-Folha-de-Pagamento-no-modulo-SIGATAF-para-an%C3%A1lise?source=search) **;**
* Arquivo XML do **GPE e TAF** **S-2299** conforme orientações do artigo: [**S-2299 - Como gerar os arquivos XML do evento S-2299 (Desligamento) no modulo SIGATAF para análise;**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006744302-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-os-arquivos-XML-do-evento-S-2299-Desligamento-no-modulo-SIGATAF-para-an%C3%A1lise?source=search)
* Arquivo XML do **GPE e TAF S-1210** com erro conforme orientações do artigo: **[S-1210 - Como gerar os arquivos XML do evento S-1210 (Pgto Rend Trab.) no modulo SIGATAF para análise](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006741342-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-gerar-os-arquivos-XML-do-evento-S-1210-Pgto-Rend-Trab-no-modulo-SIGATAF-para-an%C3%A1lise?source=search);**
* Print calculo da da rescisão (completa) e print do calculo da folha mês anterior;
* Arquivo de Fontes Conforme artigo: [**Como gerar arquivo com a data de todos os fontes do RPO;**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024518391-MP-Como-gerar-arquivo-com-a-data-de-todos-os-fontes-do-RPO?source=search)

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
