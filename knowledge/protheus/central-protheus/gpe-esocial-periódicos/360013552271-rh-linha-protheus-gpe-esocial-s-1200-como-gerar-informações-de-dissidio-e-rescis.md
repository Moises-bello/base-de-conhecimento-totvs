---
article_id: 360013552271
category: GPE - eSocial - Periódicos
content_hash: b7515d6b0e5fb0b362b14828469832e83e43f6256ac1e89e0295e67e370a411d
fetched_at: '2026-06-28T22:45:07.213039+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar informações de dissidio
  e rescisão complementar por dissidio no esocial
type: support-article
updated_at: '2026-06-26T10:43:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013552271-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-informa%C3%A7%C3%B5es-de-dissidio-e-rescis%C3%A3o-complementar-por-dissidio-no-esocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26972379263639) Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Como gerar informações de dissidio e rescisão complementar por dissidio no eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**As informações do calculo de dissidio e rescisão complementar por dissidio são geradas no evento S-1200 porem é necessário seguir as premissas abaixo:  
  
**1.** Deve existir o calculo do dissidio, mesmo para os casos que seja somente diferença de dissidio sobre o mês da rescisão:  
Caminho no SIGAGPE: *Miscelânea > Reajuste > Dissidio Retroativo (Outras Ações> Manutenção>> Informar período);***2.** Habilitar o parâmetro **MV\_ESOCDIS:**Caminho no SIGACFG: *Ambientes> Cadastros> Parâmetros;***3.** Preencher as tabelas **S050** e **S126** na rotina manutenção de tabelas:  
Caminho no SIGAGPE: *Atualizações> Definições Cálculo> Manutenção Tabelas.*

Na tabela **S050**, é efetuado relacionamento entre o tipo de aumento com o tipo de acordo do eSocial.  
**Exemplo:** Para um dissídio com tipo de aumento 003 (campo **RHH\_TIPOAUM**), é necessário possuir um registro com o campo "Tipo Aumento Tab. 41" preenchido com 003 e o campo "Tipo de Acordo eSocial" preenchido com o código do tipo de acordo.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8405144301847)  
  
Na tabela **S126**, é efetuado relacionamento entre o sindicato e data do acordo com a descrição do acordo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16175993861527)  
  
A **data acordo** é quando o acordo saiu. A **data efeito** é desde quando que esse acordo vale, a data base do sindicato. **Exemplo:**   
- Data base (informado no cadastro do sindicato): 01 (janeiro)  
- Data que saiu o acordo: 31/05/2022  
- Campo Data Acordo: 31/05/2022  
- Campo Data Efeito: 01/01/2022   
  
Boletim Técnico sobre as tabelas S050 e S126:   
<http://tdn.totvs.com/pages/viewpage.action?pageId=403050807>.  
  
No caso de duvidas sobre os registros configurados no calculo do dissidio retroativo, acesse o calculo como visualizar.

**Exemplo:** Acessando como visualizar o calculo do Dissidio de um trabalhador.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16176044657431)**4. Também deve ser verificado o campo Filial nas tabelas **S050** e **S126**, se o campo estiver preenchido a validação vai ocorrer somente para os trabalhadores da filial selecionada, apresentando erro caso exista outras Filiais com calculo de dissidio. Se o campo Filial estiver em branco a validação vai ocorrer para todas as filiais que tem o calculo do dissidio.  
  
**Observação:**  
Para trabalhadores **Ativos** e **Desligados** em meses anteriores as informações relativas a Dissidio são geradas no evento **S-1200,** através da rotina eventos periódicos na aba de "Informações relativas a remuneração do trabalhador em períodos anteriores ao período de apuração". Será necessário **integrar o roteiro RES** e **calcular** o roteiro **FOL**, para depois gerar o evento S-1200.  
Se a rescisão complementar por dissidio ocorrer no mesmo mês da primeira rescisão as informações relativas a Dissidio são geradas no evento **S-2299** que será gerado como **retificação** no momento do calculo.  
Onde os valores vão constar na aba de "**Informações relativas a remuneração do trabalhador em períodos anteriores ao período de apuração**".  
  
Para **conferencia de verbas/valores e inconsistências**, gere o relatório do evento S-1200 ou S-2299:  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no módulo GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-GPE-antes-de-integrar-o-evento-peri%C3%B3dico-para-o-TAF)  
[RH - Linha Protheus - GPE - eSocial - S-2299 - Como gerar o relatório de conferencia do evento S-2299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191)  
  
**Links Documentações Dissidio:**Para acessar a documentação completa sobre o Dissidio no evento S-1200 clique no *link*:

* [Documentação - S-1200 Geração Dissidio](http://tdn.totvs.com/x/laWbFg)
* [S-1200/S-2299 - Como registrar uma rescisão complementar no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005103432-MP-GPE-eSocial-S-1200-S-2299-Como-registrar-uma-rescis%C3%A3o-complementar-no-eSocial?source=search)
* [S-1200 - Quais verbas serão enviadas para o eSocial nos casos de Dissidio Retroativo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018355852-MP-GPE-eSocial-S-1200-Quais-verbas-ser%C3%A3o-enviadas-para-o-eSocial-nos-casos-de-Dissidio-Retroativo-?source=search)
* [Como o eSocial vai apurar os encargos nos casos de Reajuste/Dissidio Retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342453-MP-GPE-eSocial-Como-o-eSocial-vai-apurar-os-encargos-nos-casos-de-Reajuste-Dissidio-Retroativo?source=search)

**Saiba Mais**Para adquirir mais conhecimento acesse os links abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
