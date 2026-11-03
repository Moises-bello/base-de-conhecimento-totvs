---
article_id: 7405507503767
category: GPE - eSocial - Periódicos
content_hash: 1a62377d9bafee83f78cc2f60e002daa3d6383a697972ccf666b20360d2908c6
fetched_at: '2026-06-28T22:45:07.472388+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - S-5001 - Como conferir INSS por trabalhador no
  eSocial
type: support-article
updated_at: '2026-06-26T19:51:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7405507503767-RH-Linha-Protheus-GPE-S-5001-Como-conferir-INSS-por-trabalhador-no-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22851758661015) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como conferir INSS por trabalhador no eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Assista o vídeo mostrando o **passo a passo para conferencia do INSS no eSocial:** [**How To | SIGAGPE eSocial - Como Conferir INSS do RH Protheus e eSocial #TOTVS\_RH\_Linha\_Protheus**](https://www.youtube.com/watch?v=x8olU9GcAVk)

Após enviar os periódicos, o próximo passo é gerar o evento S-5001 referente ao totalizador e analisar se os valores ficaram corretos:

[RH - Linha Protheus - GPE - eSocial - S-5001 - Como realizar a conferência do evento S-5001 - Informações das contribuições sociais consolidadas por trabalhador (por CPF)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038121553-RH-Linha-Protheus-GPE-eSocial-S-5001-Como-realizar-a-confer%C3%AAncia-do-evento-S-5001-Informa%C3%A7%C3%B5es-das-contribui%C3%A7%C3%B5es-sociais-consolidadas-por-trabalhador-por-CPF-)  
  
A imagem abaixo foi retirada do site do eSocial para demonstrar valores mensais:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33514617488791)  
<https://www.gov.br/esocial/pt-br/empresas/manual-web-geral#s-5001---informa--es-das-contribui--es-sociais-consolidadas-por-trabalhador>   
  
É possível verificar que o Valor da contribuição do segurado está igual o Valor descontado do trabalhador.  
  
O **eSocial** demostra o calculo realizado através da base de calculo composta com as verbas de **Incidência 11** e aplica a **tabela de INSS vigente**, gerando o **Valor da Contribuição do Segurado.**  
  
O **campo Valor Descontado do Trabalhador** é composto pelos valores das verbas enviadas com **rubrica 31 (Contribuição descontada do segurado)**.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7405062260759)  
  
O eSocial monta a própria base de cálculo de acordo com a incidência que enviamos referente ao campo INSS eSocial, como 11 (base de calculo do salario de contribuição mensal) por exemplo e esse valor deve bater com o valor da base de INSS da folha ou de férias por exemplo.  
  
Lembrando que mostramos um exemplo de valores mensais, por exemplo para 13º devemos analisar suas respectivas rubricas.  
  
**2.** Para que possamos conferir as rubricas cadastradas no sistema para cada verba, a incidência do INSS para folha, os valores por verba, o tipo da verba, é necessário realizar a conferência através do **relatório S-1200:**  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no GPE antes de integrar o evento periódico para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334)  
[RH - Linha Protheus - GPE - eSocial - S-2299 - Como gerar o relatório de conferencia do evento S-2299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191)  
  
Através do relatório conseguimos filtrar pela chave ideDmDev e selecionar somente os cálculos de Férias, folha, ou adiantamento.  
No exemplo abaixo filtrei somente para a chave com valores de folha. Nesse cenário temos o código da verba, o tipo, valor, natureza, Incidência INSS eSocial e Incidência INSS folha:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7405293177111)  
  
Devemos sempre **analisar** se os **valores gerados nos cálculos estão corretos**, pois se base de INSS ou o desconto estiver com valor errado, para o eSocial os valores também ficarão incorretos.  
Essa analise pode ser realizada antes de enviar os eventos periódicos, caso considere necessário.  
  
Podem existir Verbas/Rubricas na sua Folha de Pagamento do SIGAGPE que não estão informadas no evento S-1200, para solucionar esse problema efetue as validações indicadas nos artigos abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Minha verba não aparece no evento S-1200, como saber se ela está configurada no Protheus como verba de diferença de Dissidio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035981593-RH-Linha-Protheus-GPE-eSocial-S-1200-Minha-verba-n%C3%A3o-aparece-no-evento-S-1200-como-saber-se-ela-est%C3%A1-configurada-no-Protheus-como-verba-de-diferen%C3%A7a-de-Dissidio)  
[RH - Linha Protheus - GPE - eSocial - S-1200 / S-1210 - Como verificar qual foi motivo de uma verba ou valor não ser gerado no evento S-1200 ou S-1210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004986951-RH-Linha-Protheus-GPE-eSocial-S-1200-S-1210-Como-verificar-qual-foi-motivo-de-uma-verba-ou-valor-n%C3%A3o-ser-gerado-no-evento-S-1200-ou-S-1210)  
  
**3.** Com base nas informações do relatório, devemos conferir também o que foi enviado ao eSocial, se condiz com a parametrização do sistema.  
**Os dados enviados no evento S-1010 é a forma que o governo vai calcular os valores de INSS.**  
Qualquer alteração de verbas, deve ser feita no Protheus e depois enviado ao eSocial.   
[RH - Linha Protheus - GPE - eSocial - S-1010 - Como consultar no site do eSocial dados do evento S-1010 (Tabelas de Rubricas)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043153534-RH-Linha-Protheus-GPE-eSocial-S-1010-Como-consultar-no-site-do-eSocial-dados-do-evento-S-1010-Tabelas-de-Rubricas-)  
  
Portanto devemos analisar as verbas enviadas ao eSocial no evento S-1200 por exemplo e conferir as rubricas que estão com incidência no campo Cd. Inc. Cp, do cadastro de verbas (SRV), aba eSocial e confrontar com as informações enviadas ao eSocial através do evento S-1010.  
  
Abaixo exemplo do campo Cd. Inc. CP  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7403844661399)  
Exibição do conteúdo do evento, retirado do manual do eSocial:   
<https://www.gov.br/esocial/pt-br/empresas/manual-web-geral#s-1010---tabela-de-rubricas>

Exemplo da Incidência Tributaria - Previdência Social. Contem data de inicio da rubrica e número de recibo.  
![12TabelaRubricasexibido.png](https://www.gov.br/esocial/pt-br/empresas/manual-web-geral/figuras-manual/12TabelaRubricasexibido.png/@@images/6be5c3fe-aa06-4e03-8bb6-f555206c5c67.png)  
  
[RH - Linha Protheus - GPE - eSocial - S-5001 - Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512-RH-Linha-Protheus-GPE-eSocial-S-5001-Como-ajustar-incid%C3%AAncia-e-validade-de-rubricas-no-governo-TAF-e-GPE)  
  
**Atenção**  
É de extrema importância identificarmos exatamente onde está o valor incorreto, na folha, em férias, no portal do eSocial ou no S-5001.  
  
**Saiba mais**  
Para saber mais consulte os *links*abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-1200 - O INSS e FGTS fica incorreto no eSocial (DCTFWEB) quando existe Férias no mês](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422759630487-RH-Linha-Protheus-GPE-eSocial-S-1200-O-INSS-e-FTGS-fica-incorreto-no-eSocial-DCTFWEB-quando-existe-F%C3%A9rias-no-m%C3%AAs?source=search)  
[Painel de Conferência INSS: Versão FULL #TOTVS\_Backoffice\_Linha\_Protheus](https://www.youtube.com/watch?v=0-fQNaGPdIA&t=9s)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****"*  
*Quer receber**em primeira mão sobre artigos publicados? Participe da nossa* [***Comunidade******WhatsApp***](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
