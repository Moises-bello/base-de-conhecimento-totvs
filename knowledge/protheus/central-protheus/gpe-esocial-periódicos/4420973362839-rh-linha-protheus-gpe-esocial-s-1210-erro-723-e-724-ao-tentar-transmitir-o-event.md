---
article_id: 4420973362839
category: GPE - eSocial - Periódicos
content_hash: 820eec1bb3fbeaa2dccfd135838ef32ad8a7c0d924795148f028e7964bd76576
fetched_at: '2026-06-28T22:45:08.945361+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210 - Erro 723 e 724 ao tentar transmitir
  o evento S-1210 para o eSocial
type: support-article
updated_at: '2024-08-28T21:17:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420973362839-RH-Linha-Protheus-GPE-eSocial-S-1210-Erro-723-e-724-ao-tentar-transmitir-o-evento-S-1210-para-o-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21577245749655) Tempo aproximado para leitura: **05:00:00 min****Ocorrência**Erro 723 e 724 ao tentar transmitir o evento S-1210 para o eSocial  
  
**Tipo: Advertência - Código da Ocorrência: 723** - Descrição : Valor Liquido invalido. O valor esperado do trabalhador CPF: xxxxxxxxxxx e: (xxx,xx).Ação Sugerida: Em caso de pagamento total, o valor liquido deve corresponder ao somatório dos valores de vencimentos e descontos da remuneração e também dos descontos de IRRF e Pensão alimentícia. Em caso de pagamento parcial, o valor liquido deve corresponder ao somatório dos valores de vencimentos e descontos informados no grupo infoPgtoParc.  
  
**Tipo: Erro - Codigo da Ocorrência: 724** - Descrição : Nao foi localizado um evento de remuneracao do trabalhador para o periodo e com mesmo demonstrativo de pagamento.Acao Sugerida:Deve ser um valor atribuido pela fonte pagadora em S-1200, S-1202 ou S-1207 no campo quot;Identificador de Recibo de Pagamentoquot;, obedecendo a relacao:.Se Tipo de Pagamento = [1], em S-1200;.Se Tipo de Pagamento = [5], em S-1202;.Se Tipo de Pagamento = [6], em S-1207.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**Quando o governo retorna o erro **723 "Valor Líquido inválido"** atrelado aos erros **724 "Não foi localizado um evento de remuneração"** o problema esta relacionado ao identificador de pagamento do S-1200 que não foi localizado no site do eSocial.  
  
Todo evento **S-1200** (Remuneração de trabalhador), **S-1202** (Remuneração de servidor), **S-2299** (Desligamento) e **S-2399** (Desligamento Trabalhador sem Vinculo), tem um identificador para o demonstrativo de pagamento denominado no XML com a **tag** *ideDmDev* que é a chave do recibo do pagamento apresentado no campo **Iden Dem Pgt/Vl** dentro do **S-1210***.*

Para que o evento **S-1210** (Pagamento Rendimentos) seja aceito pelo *RET* é necessário que exista protocolado no *RET* um evento **S-1200**, **S-1202**, **S-2299** ou **S-2399** com mesmo tag/chave *ideDmDev* (**Iden Dem Pgt/Vl**)gerado no **S-1210** referente ao mesmo período de apuração.  
  
Nesse caso sempre que existir no S-1210 a tag/chave *ideDmDev* (**Iden Dem Pgt/Vl**) ausente ou incorreta vai acontecer esse erro na transmissão.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Caso seja o inicio da obrigação dos eventos periódicos (primeiro mês de envio do S-1200 de acordo com o **cronograma oficial** para o seu grupo de empresas) verifique o conteúdo do parâmetro **MV\_DTCGINI** esse parâmetro deve ter a data que a empresa iniciou a entrega dos eventos não periódicos de acordo com o cronograma do governo, e vai influencias no primeiro mês de geração dos eventos periódicos. Caso não seja o seu cenário pule para o item 2.  
  
**2.** Verifique no TAF e no governo se foi enviado no **S-1200** o recibo referente a folha de pagamento. Se for regime caixa deve ser verificado o mês anterior. Ocorre muitos problemas onde o cliente envia para o governo apenas o recibo de adiantamento no **S-1200** ocasionando erro no **S-1210**.  
  
**Como verificar no TAF:**  
Acesse no TAF (84) no caminho: atualizações > eventos eSocial > periódicos > folha de pagamento **(TAFA250)**. Entre no **S-1200** do trabalhador no mês de geração atual e mês anterior e verifique na aba Demonstrativos de Valores se tem na grid com nome **Iden Dem Pgt** uma linha com o código onde as 3 ultimas letras são **FOL**.![S-1200_taf.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4420955234967)  
  
Caso exista não a chave com final **FOL** é possível que não tenha sido enviado para o governo as informações referentes a folha desse trabalhador. Avalie se realmente não foi enviado o pagamento no S-1200 com a chave **FOL** no mês referente ao S-1210, e no S-1200 do mês anterior (empresas que trabalham com regime de caixa).  
  
Se o erro estiver no S-1200 do mês de atual, ou seja não tem a informação **FOL** gere novamente o evento S-1200 marcando no GPE a opção "**considerar dados do período em aberto**". Se o erro for referente a um S-1200 do mês anterior ou mês fechado no eSocial será necessário reabrir a folha no governo **(apenas folha eSocial e não folha Protheus)** e reenviar o evento, pois nem os dados da previdência para esse trabalhador foram recolhidos.  
  
Material com orientações:

* [Como retificar eventos S-1200 ou S-1210 que já foram transmitido para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000230862)
* [Como retificar ou reprocessar os Totalizados (DCTFWEB) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025678254)
* [Como consultar no site do eSocial dados do evento S-1200 (Folha de Pagamento)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043290614)

**3.** Verifique se o sistema está atualizado com o ultimo pacote de expedição continua do RH, pois sempre que ocorre erro no fonte relacionado ao evento S-1210 a atualização é gerada no pacote de expedição.  
Link: **[Pacote e Dicionário Correções Expedição Continua RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)**  
  
**Atenção**  
Após atualizar o sistema é necessário **excluir** o S-1210 e gerar novamente.  
Consulte nosso material: [Como excluir do TAF em lote / massiva os Eventos Periódicos sem protocolo e/ou inconsistentes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035240653)  
  
**4.** Se o erro continuar ocorrendo mesmo após a analise de todos os itens anteriores encaminhe as seguintes informação para analise do suporte técnico.   
  
Encaminhar os dados abaixo de **apenas um trabalhador**:

* Arquivo XML do **GPE e TAF** **S-****1200**mês anterior conforme orientações do artigo:[**S-1200 - Como gerar os arquivos XML do evento S-1200 (Folha de Pagamento) no modulo SIGATAF para análise**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006729801-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-os-arquivos-XML-do-evento-S-1200-Folha-de-Pagamento-no-modulo-SIGATAF-para-an%C3%A1lise?source=search) **;**
* Arquivo XML do **GPE e TAF** **S-1200** do mês atual conforme orientações do artigo: [**S-1200 - Como gerar os arquivos XML do evento S-1200 (Folha de Pagamento) no modulo SIGATAF para análise;**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006729801-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-os-arquivos-XML-do-evento-S-1200-Folha-de-Pagamento-no-modulo-SIGATAF-para-an%C3%A1lise?source=search)
* Arquivo XML do **GPE e TAF S-1210** com erro conforme orientações do artigo: **[S-1210 - Como gerar os arquivos XML do evento S-1210 (Pgto Rend Trab.) no modulo SIGATAF para análise](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006741342-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-gerar-os-arquivos-XML-do-evento-S-1210-Pgto-Rend-Trab-no-modulo-SIGATAF-para-an%C3%A1lise?source=search);**
* Relatório **S-1200** conforme orientações do artigo: [**Como gerar relatório de conferência do evento S-1200 no GPE antes de integrar o evento periódico para o TAF;**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-GPE-antes-de-integrar-o-evento-peri%C3%B3dico-para-o-TAF?source=search)
* Print calculo da folha mês atual e mês anterior;
* Arquivo de Fontes Conforme artigo: [**Como gerar arquivo com a data de todos os fontes do RPO;**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024518391-MP-Como-gerar-arquivo-com-a-data-de-todos-os-fontes-do-RPO?source=search)
* Informe como está definido o seu parâmetro **MV\_TAFVLES** e **MV\_VLESOC.**

**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
