---
article_id: 37108578059927
category: GPE - eSocial - Carga Inicial
content_hash: 2289d82842da9d6c971ff09c5dcf4496dcefd0b6614182fcb5d50a56eaefaabc
fetched_at: '2026-06-28T22:45:03.041102+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Como se adequar e atualizar o ambiente
  para Nota Técnica 04/2025 leiaute S-1.3 referente a Natureza de Rubrica 1015
type: support-article
updated_at: '2026-06-24T15:14:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37108578059927-RH-Linha-Protheus-GPE-eSocial-Como-se-adequar-e-atualizar-o-ambiente-para-Nota-T%C3%A9cnica-04-2025-leiaute-S-1-3-referente-a-Natureza-de-Rubrica-1015
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37108593287319) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como se adequar e atualizar o ambiente para Nota Técnica 04/2025 leiaute S-1.3 referente a Natureza de Rubrica 1015 (Rotina de substituição de verbas).   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
***Playlist*** **de videos curtos ensinando como conferir as incidências, calculo da folha e calculo das férias:**

**Treinamento realizado sobre a nova natureza, mostramos o cadstro de verbas, calculos e envio ao esocial:**

Para atender a necessidade do **item 3.3 da Nota Técnica 04/2025** do eSocial leiaute S-1.3 referente a **Natureza de Rubrica 1015 - Adiantamento de Férias**. Será realizado a substituição das verbas de férias, transitadas no calculo de Folha de Pagamento, geradas no evento S-1200.  
  
Cada verba calculada no Roteiro de Férias, terá sua respectiva verba de eSocial, uma para Férias pagas no mês de Gozo e outra para Férias pagas no mês Anterior (somente naturezas 1016 e 1017).  
  
A verba será definida no Cadastro de Verbas, e será gerada nas tabelas de movimentação SRR / SRD / SRC / RGB no campo XX\_FERSUB.  
  
**Atualizações necessárias**  
- Aplicar pacote [**Expedição Continua RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=501123489#issues-17) a partir de 08/12/2025, atualizar o **Dicionário de Dados (**execução do **UPDDISTR);**  
- Aplicar pacote [**Expedição Continua TAF**](https://tdn.totvs.com/pages/releaseview.action?pageId=634272553&draft=true#issues-17);  
- **Atualizar as autocontidas** do **TAF**: [Atualização das tabelas autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034479973-Automa%C3%A7%C3%A3o-Fiscal-CONFIGURA%C3%87%C3%83O-Atualiza%C3%A7%C3%A3o-das-tabelas-autocontidas?source=search)  
  
**Procedimento**  
**1º Passo**  
Atualizar a Tabela S047-Natureza de Rubrica (**Natureza 1015**) - [Como atualizar as tabelas S047, S048, S049, S054, S056 e S057, quando existe alteração das tabelas oficias no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034614474-RH-Linha-Protheus-GPE-eSocial-Como-atualizar-as-tabelas-S047-S048-S049-S054-S056-e-S057-quando-existe-altera%C3%A7%C3%A3o-das-tabelas-oficias-no-eSocial)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37108593287703)  
  
**2º Passo**  
 Cadastro de Verbas - Disponibilizado facilitador para criação de novas verbas de férias que substituirão as verbas no demonstrativo FER dos eventos S-1200/S-2299. A rotina de Substituição das Verbas de Férias será disponibilizada como opção do Cadastro de Verbas (GPEA040 > Outras Ações).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37108578045719)  
  
Ao acessar, serão carregadas as verbas configuradas como **RV\_REFFER=S**, com incidência de IR **RV\_INCIRF=13, 33, 43, 53 e 48.**  
  
**Para o INSS:**  
\*\* Id **0065**: RV\_REFFER = S, RV\_INCIRF = 9, RV\_INCCP = 31.   
\*\* Id **0168**: RV\_REFFER = S, RV\_INCIRF = 43, RV\_INCCP = 00.  
  
Será informada a quantidade de registros encontrados para substituição, e questionado ao usuário se deseja que a rotina sugira os novos códigos ou prefere informar manualmente  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37108593289111)  
  
Selecionando (Sim), serão carregadas as informações das verbas atuais nas primeiras 5 colunas, e nas restantes, listará os códigos/descrições sugeridos para as novas verbas que serão criadas  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37108593289495)  
**Observação**: Caso opte por informar os novos códigos manualmente, as colunas '**Novo Cód.Verba**' e '**Verba PG MES ANT**' estarão em branco e devem ser preenchidas para efetuar o processamento.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37108593290647)  
  
Ao final será gerado log do processamento, listando todas as verbas envolvidas. Tanto as verbas existentes quanto as novas terão seu conteúdo atualizado, com integração dos eventos S-1010 correspondentes.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37108593290903)  
  
**Exemplo**  
Cadastro da verba 129 (Id 0072), foram criadas as verbas 799 e 856  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37108593291287)  
  
Neste exemplo, será gerado três eventos S-1010:  
Verba de Férias (129), pois a Incidência IRRF foi retirada;  
Verba de Substituição - **Vb Fer Mes** (799) com incidência IRRF 13;  
Verba de Substituição - **Vb Fer Mes A** (856) com incidência IRRF 13;  
  
**3º Passo**  
Calculo de Férias com pagamento no mês de gozo das Férias, será gravado no campo **Vd Subs. Fer** o código da verba **Vb Fer Mes.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/37108593291671)**  
  
Calculo de Férias com pagamento no mês anterior ao gozo das Férias, será gravado no campo **Vd Subs. Fer** o código da verba **Vb Fer Mes A.**  
  
**Pontos de** **Atenção:**  
- No parâmetro **MV\_DTINFER** será gravada a competência de envio informada durante a execução, obedecendo o compartilhamento da tabela de verbas SRV;  
- O campo **Verba PG MES ANT (**RV\_FERAXML**)** só será preenchido para as verbas cuja Natureza for 1016 ou 1017, as demais NÃO terão este campo preenchido;  
- No calculo das Férias, o campo Vb Subs.Fer (RR\_FERSUB) será preenchido pelo conteúdo do **Vd Subs. Fer** (férias paga no mês) ou pelo conteúdo do campo **Vb Fer Mes A** (férias paga no mês anterior). Porém, caso as férias seja paga no mês anterior e o campo **Vb Fer Mes A** esteja vazio, será preenchido com o conteúdo do campo **Vd Subs. Fer.** E se ambos estiverem vazio, será preenchido com a verba original.   
  
Para mais informações, acesse o **Boletim Técnico** abaixo:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=1016690512>  
  
Caso o **cálculo de ferias tenha sido realizado sem a criação das verbas de substituição**, realize o cadastro das verbas conforme passo a passo acima e **recalcule as ferias**.   
  
Para **férias que não podem ser recalculadas**, utilize o Rdmake [**UPDFERSUB**](https://tdn.totvs.com/pages/releaseview.action?pageId=1014630057#body-body2)que fará a inclusão das verbas de substituição no cálculo das ferias, sem precisar recalcular.   
Necessário compilar o Rdmake dos links abaixo:  
12.1.2310:<https://r.totvs.io/p/1238079> ;   
12.1.2410:<https://r.totvs.io/p/1238077> ;   
12.1.2510:<https://r.totvs.io/p/1238078> ;  
  
\* Para criação manual do menu do rdmake, verifique a imagem em anexo.  
  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
