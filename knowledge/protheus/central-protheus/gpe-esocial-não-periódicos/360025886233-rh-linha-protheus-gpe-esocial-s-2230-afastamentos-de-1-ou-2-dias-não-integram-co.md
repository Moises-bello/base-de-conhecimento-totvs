---
article_id: 360025886233
category: GPE - eSocial - Não Periódicos
content_hash: 8be6f034bdd53fd04320a12395027d9cb657742ad3d7280f9bf0a46a9940f794
fetched_at: '2026-06-28T22:45:04.818804+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2230 - Afastamentos de 1 ou 2 dias
  não integram com o TAF
type: support-article
updated_at: '2026-06-16T11:24:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025886233-RH-Linha-Protheus-GPE-eSocial-S-2230-Afastamentos-de-1-ou-2-dias-n%C3%A3o-integram-com-o-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41259070041495) Tempo aproximado para leitura: 00:01:00**  
  
**Dúvida**  
Ao inserir no cadastro de ausências 1 ou 2 dias de atestado para o funcionário, o mesmo não é enviado ao TAF.   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Conforme orientação do MOS - Manual de Orientações do eSocial, os afastamentos serão enviados ao TAF automaticamente, se forem maiores ou iguais a 3 dias. No caso de afastamentos referente ao mesmo motivo de 1 ou 2 dias que somados totalizem um valor **maior** que 15 dias, será enviado o evento S-2230 referente a todos os afastamentos do colaborador.  
  
![](https://totvssuporte.zendesk.com/attachments/token/QXlq6AmCWww5CNiqIStYeasWn/?name=inline1458026187.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/Z9GjLgTwNpzlzn2yRYTAfg8kF/?name=inline1817358829.png)   
  
**Exemplo**:   
  
**Passo 1:**  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040064934)  
O registro é salvo, porém não ocorre integração com o TAF.   
  
**Passo 2:**  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040895313)  
  
Incluímos um novo atestado de 13 dias referente ao mesmo motivo que será integrado devido ser maior que 3 dias. Podemos notar que até o momento, a somatória gerou 15 dias.   
  
**Passo 3:**  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040895733)  
  
Após incluir 1 dia de afastamento referente ao mesmo motivo, automaticamente ocorre a integração com o TAF e todos os registros são enviados:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040894933)  
  
Para casos onde se entende encessário a integração de afastamentos com menos de 3 dias, será preciso habilitar o parametro **MV\_AFA3DIA**. Veja o boletim tecnico: <https://tdn.totvs.com/pages/releaseview.action?pageId=622211571>  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[*TOTVS Informa*](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
