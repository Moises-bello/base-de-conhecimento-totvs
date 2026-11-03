---
article_id: 360024125112
category: GPE - eSocial - Periódicos
content_hash: 1bac3a547746977c7cccc68c2bb18b4203447966739efc69341edc68051b3ae9
fetched_at: '2026-06-28T22:45:07.399723+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210 - Inconsistência do RET - 723,
  724, 726 no retorno do evento transmitido ao governo
type: support-article
updated_at: '2025-07-24T13:14:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024125112-RH-Linha-Protheus-GPE-eSocial-S-1210-Inconsist%C3%AAncia-do-RET-723-724-726-no-retorno-do-evento-transmitido-ao-governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27501638604055)Tempo aproximado para leitura: **00:02:00min  
  
Ocorrência**Código da Ocorrencia: 401 - Conteúdo do evento inválido. Erros 723, 724, 726 no retorno do evento transmitido ao governo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Quando o governo retorna o erro **723 "Valor Líquido inválido"** atrelado aos erros **724 "Não foi localizado um evento de remuneração"** ou **726 "Não foi localizado um evento de rescisão contratual"** o problema pode estar relacionado ao identificador de pagamento.  
  
Todo evento **S-1200** (Remuneração de trabalhador), **S-1202** (Remuneração de servidor), **S-2299** (Desligamento) e **S-2399** (Desligamento Trabalhador sem Vinculo), tem um identificador para o demonstrativo de pagamento denominado no XML com a **tag** *ideDmDev* que é a chave do recibo do pagamento apresentado no campo **Iden Dem Pgt/Vl** no **TAF***.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27501651794199)*

Para que o evento **S-1210** (Pagamento Rendimentos) seja aceito pelo *RET* é necessário que exista protocolado no *RET* um evento **S-1200**, **S-1202**, **S-2299** ou **S-2399** com mesmo tag/chave *ideDmDev* (**Iden Dem Pgt/Vl**)gerado no **S-1210** referente ao mesmo período de apuração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27501638609559)

**Exemplo pagamento regime caixa:**Folha de agosto com pagamento em 05/09/2024.

1. **S-1200** (competência **08/2024**): Vai Trazer as chaves *ideDmDev*da folha com os pagamentos do mês;
2. **S-1210** (competência **08/2024**): Vai Trazer as chaves *ideDmDev* somente dos **valores pagos** de 01 a 31/08/2024, ou seja, não terá o pagamento que ocorreu em 05/09/2024;
3. **S-1210** (competência **09/2024**): Vai Trazer as chaves *ideDmDev* somente dos **valores pagos** de 01 a 30/09/2024, ou seja, o valor da folha de agosto/2024 pago em 05/09/2024 vai estar no evento S-1210 de 09/2024.

**Exemplo pagamento regime competência:**Folha de agosto com pagamento em 31/08/2024.

1. **S-1200** (competência **08/2024**): Vai Trazer as chaves *ideDmDev*da folha com os pagamentos do mês;
2. **S-1210** (competência **08/2024**): Vai Trazer as chaves *ideDmDev* somente dos valores pagos de 01 a 31/08/2024, ou seja, terá o pagamento que ocorreu em 31/08/2024.

Os **tipos (código) de pagamento** que possuem tag/chave **ideDmDev**, estão relacionados abaixo, por isso é importante verificar se o erro está ocorrendo para esses tipos de pagamento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27501651797015)

**Solução**Verificar se o conteúdo do campo **ideDmDev** e **Tipo Pgto** está igual entre os eventos **S-1200** e **S-1210**, ou quando existir rescisão verificar os eventos **S-2299** e **S-1210**.   
  
Caso o erro não seja solucionado com os artigos mapeados encaminhar as informações abaixo para analise do suporte:

* Informar a qual grupo a empresa pertence no **eSocial**, ex: 1º grupo > 78 milhões, 2º grupo < 78 milhões, 3º grupo optante pelo simples;
* Arquivo *XML* do **GPE** e **TAF**. Consulte o link [MP - GPE - eSocial - Como gerar ou comparar os arquivos XML do SIGAGPE e SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026656853) ou o  link [Como exportar XML de eventos do esocial?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006744012;);
* Arquivo com data de todo os fontes. Consulte o link [Como gerar arquivo com a data de todos os fontes?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024518391);
* Print ou vídeo parâmetro MV\_DTCGINI;
* Se for erro 726 print do calculo da rescisão no GPE;
* Print ou vídeo do evento S-1200 aba demonstrativo de verbas onde é apresentado o campo **Iden Dem Pgt**no **TAF**;
* Print ou vídeo do evento S-1210 aba demonstrativo de verbas onde é apresentado o campo **Iden Dem Vl** no **TAF**;
* Print ou vídeo do evento S-2299 aba demonstrativo de verbas onde é apresentado o campo **Iden Dem Vl** no **TAF**;

**Saiba Mais**Para saber mais consulte os links abaixo:   
[S-1210 - 723 / 724 - Em meses onde houve calculo de 13º salario e rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020613312)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
