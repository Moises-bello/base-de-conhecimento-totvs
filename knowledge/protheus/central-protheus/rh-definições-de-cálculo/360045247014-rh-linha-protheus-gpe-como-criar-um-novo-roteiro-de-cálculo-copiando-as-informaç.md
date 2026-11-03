---
article_id: 360045247014
category: RH - Definições de Cálculo
content_hash: 43f50d9fe39a3e205450d4d09f5eeaeeed1772ab3eaaa5a7aaed5e6c205f1763
fetched_at: '2026-06-28T22:43:22.373830+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Como criar um novo roteiro de cálculo copiando
  as informações de outro roteiro já existente
type: support-article
updated_at: '2025-10-03T18:17:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045247014-RH-Linha-Protheus-GPE-Como-criar-um-novo-roteiro-de-c%C3%A1lculo-copiando-as-informa%C3%A7%C3%B5es-de-outro-roteiro-j%C3%A1-existente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35391053921303) Tempo aproximado para leitura: 00:02:00 min****Dúvida**Como criar um novo roteiro de cálculo copiando as informações de outro roteiro já existente?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**A copia de roteiro de calculo possibilita criar um novo roteiro com todos os dados do roteiro selecionado, sendo uma **customização do usuário** e **não padrão do sistema.** Esse processo se for realizado de forma indevida pode alterar a forma dos de calculo do sistema, por isso deve ser realizado apenas por um usuário que conheça os processos e suas implicações.  
  
Para criar um novo roteiro com copia de dados de outro roteiro acesse o caminho: **Atualizações> Definições de Cálculo> Roteiros de Cálculo**. Posicione em cima do roteiro a ser copiado e clique em **Outras Ações/Copia:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063809613)

Será aberta um tela com todos os dados do roteiro no qual será feita a copia, onde deve ser definido o nome e descrição do novo roteiro:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062907314)  
  
  
Após esse processo o novo roteiro será criado com a legenda verde (definido pelo usuário):  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062907374)  
  
  
Com isso o usuário pode vincular esse roteiro de cálculo ao cadastro de períodos para que seja habilitado para cálculos.  
  
**Exemplo**:  
- Caminho **Atualizações> Definições de Cálculo> Períodos**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063810253)  
 **Importante:** O atendimento do suporte padrão Protheus não auxilia em customizações.  
  
**Observações**A chave para qualquer cálculo e lançamento, na versão 12, é: Processo + Período + Número de Pagamento + Roteiro.  
  
O processo serve como agrupador de funcionários no momento dos cálculos. Os funcionários são agrupados de acordo com o tipo de cálculo que possuem, por exemplo, celetistas mensalistas são agrupados em processo diferente dos celetistas semanalistas.

Os períodos são o espaço de tempo que o cálculo deve abranger para o processamento. Seu código é constituído por ano e mês.[Por exemplo, para realizar o cálculo de funcionários mensalistas no mês de janeiro/2015 é necessário cadastrar um período iniciado em 01/01/2015 a 31/01/2015. O código do período será 201501]  
  
O número de pagamento viabiliza a divisão do período em diversos intervalos de pagamento. Utilizado, por exemplo, para pagamento de semanalistas (4 pagamentos em um mesmo mês).

O roteiro indica qual cálculo será realizado.  
  
  
  
**Saiba Mais**  
[MP - GPE - Como funciona cadastro de Períodos e Roteiros de Cálculo na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004425452)
