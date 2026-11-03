---
article_id: 360050354873
category: RH - Relatórios
content_hash: c1a1f75aad27b78d376c72b5a82755d15864e7712f466138606b646624154271
fetched_at: '2026-06-28T22:44:43.547489+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Funcionalidade do espelho de ponto fiscal - PONR140
type: support-article
updated_at: '2026-02-06T20:06:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050354873-RH-Linha-Protheus-PON-Funcionalidade-do-espelho-de-ponto-fiscal-PONR140
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38226559407255)****Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Qual a funcionalidade do espelho de ponto fiscal - PONR140?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Este relatório contempla o posicionamento dos campos definidos na Portaria **MTE 1.510.**  
Além disso, os tratamentos realizados sobre as marcações do funcionário também são exibidas.  
O espelho de ponto **PONR140**, traz as marcações originais do funcionários mediante informações constantes na tabela **RFE**.  
  
**Especificações das colunas do Espelho de Ponto**  
**1.** Coluna **“Dia”:** Data em que foram marcados os horários;  
**2.** Coluna **“Marcações Registradas no Ponto Eletrônico”:** Todos os horários existentes no arquivo original na linha relativa à data em que foi efetuada a marcação;  
**3.** Coluna **“Jornada Realizada”:** Horários tratados (originais, incluídos ou pré-assinalados);  
**\*\***observando sempre o par **“Entrada/Saída”:** Quando uma jornada de trabalho iniciar em um dia e terminar no dia seguinte, serám utilizadas duas linhas para a mesma jornada. Neste caso a data será repetida;  
**4.** Coluna **“CH”:** Código do horário contratual;  
**5.** Coluna **“Tratamentos efetuados sobre os dados originais”:**  
**5.1.** O campo **“Horário**” terá informações do horário tratado;  
**5.2.** O campo **“Ocor.”** (ocorrência) com **“D”** quando o horário for **desconsiderado**, **“I”** quando o horário for **incluído** e **“P”** quando houver a **pré-assinalação** do período de repouso.   
**5.3.** O campo **“Motivo”** deve ser preenchido com um texto que expresse o motivo da inclusão ou de ser descondiderado cada horário marcado com ocorrência **“I”** ou **“D”**.   
**5.4.** O campo **“Motivo”** não terá informações quando o campo **“Ocorrência”** for preenchido com “P”. [DOU 25/08/2009 – Seção I](https://www.jusbrasil.com.br/diarios/DOU/2009/08/25/Secao-1).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38226570774295)  
  
**Veja mais em**  
<http://www.trtsp.jus.br/geral/tribunal2/ORGAOS/MTE/Portaria/ANEXOI_PORT_1510_MTE.pdf>  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
