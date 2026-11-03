---
article_id: 360015816272
category: RH - Relatórios
content_hash: ec88afae5291fd3617775e7815fe95c20c2ea963353d8f29172727a3505b1e0f
fetched_at: '2026-06-28T22:44:43.542756+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Forma de contabilização do Banco de Horas no Espelho
  de Ponto
type: support-article
updated_at: '2026-03-17T18:31:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015816272-RH-Linha-Protheus-PON-Forma-de-contabiliza%C3%A7%C3%A3o-do-Banco-de-Horas-no-Espelho-de-Ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33723242817047) Tempo aproximado para leitura: 01:00:00 min  
  
Dúvida**Forma de contabilização do **Banco de Horas no Espelho de Ponto.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O **Espelho de Ponto** utiliza a pergunta Imprime Banco de horas, para demonstração e composição do saldo de banco de horas — tanto anterior quanto o atual —, bem como o saldo crédito e débito do período gerado. Valida os períodos com base nos parâmetros **MV\_PAPONTA** e **MV\_PONMES**. Para que não haja divergência em relação à contabilização apresentada no **Relatório de Banco de Horas**, deverá levar em consideração os períodos de apontamento para que seja gerado de forma correta.  
Para maiores detalhes veja [Como imprimir o Espelho de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004253171-RH-Linha-Protheus-PON-Como-imprimir-o-Espelho-de-Ponto)  
  
O saldo de banco de horas exibido no espelho de ponto serve apenas como conferência, baseado no saldo anterior e saldo atual do período gerado. Essa funcionalidade **não apresenta o mesmo nível de detalhamento** que o [Relatório de Banco de Horas.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000460762-RH-Linha-Protheus-PON-Como-Gerar-o-Relat%C3%B3rio-de-Banco-de-Horas-Formato-Excel-Impress%C3%A3o-em-Sint%C3%A9tico-ou-Anal%C3%ADtico)

Para garantir a consistência do saldo do banco de horas no espelho de ponto em relação às movimentações do banco de horas do funcionário, é fundamental validar:

* Se já existem horas baixadas;
* A **Data da Baixa** do banco de horas, que deve corresponder ao último dia do período fechado.

Essa data, preferencialmente, é preenchida automaticamente durante a execução do [fechamento do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013670411-RH-Linha-Protheus-PON-Como-efetuar-o-fechamento-do-banco-de-horas), com base na opção **“Data de Pagamento Folha?”**.

Suponha que o espelho de ponto seja gerado para o período de apontamento é **15/03 até 14/04**. O relatório considerará somente as movimentações do banco de horas dentro desse intervalo.

* O campo **Saldo Anterior** refletirá o saldo apurado no período anterior, ou seja, de **15/02 até 14/03**.
* Se houver movimentações do banco de horas até **14/03**, mas com data de baixa em **16/03**, o saldo anterior será exibido no espelho, pois as movimentações têm data de baixa dentro do período do espelho gerado.

No espelho padrão utiliza como parâmetro o conteúdo do período de apontamento **MV\_PONMES**.  
Portanto, para o correto uso do fechamento do banco de horas, recomenda-se que a baixa seja realizada com a **“Data de Pagamento Folha?”** igual ao último dia do período processado e refletido no parâmetro **MV\_PONMES**.

Para garantir a precisão das informações e transparência com o funcionário, recomenda-se:

* Gerar o **Relatório de Banco de Horas** ou **Extrato de Banco de Horas;**
* Conferir os dados do relatório junto com o **Espelho de Ponto**;
* Apresentar as informações combinadas ao funcionário, quando necessário.

O espelho de ponto possui a seção Banco de horas para conferência que consiste nas opções detalhadas a seguir:  
Saldo Anterior->saldo anterior das horas normais e acumuladas até a data imediatamente anterior ao primeiro dia do período que está gerando o espelho de ponto;  
Saldo Anterior Valorizado->saldo anterior das horas valorizadas e acumuladas até a data imediatamente anterior ao primeiro dia do período que está gerando o espelho de ponto;  
Débito->Total das horas negativas do período gerado no espelho;  
Crédito->Total das horas positivas do período gerado no espelho;  
Saldo Atual->valor obtido ao confrontar o cálculo do Débito com o do Crédito, somando ou subtraindo o saldo anterior conforme aplicável;  
Saldo Atual Valorizado->valor apresentado do cálculo da coluna de horas valorizadas, ajustado pela soma ou subtração do Saldo Anterior Valorizado;

**Saiba Mais**  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[RH - Linha Protheus - PON - Horas Valorizadas no Espelho de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402768068887-RH-Linha-Protheus-PON-Horas-Valorizadas-no-Espelho-de-Ponto)  
[Saldo de Banco de Horas Valorizado](https://tdn.totvs.com/display/public/PROT/DT+Viabilizar+o+Saldo+de+Banco+de+Horas+Valorizado+Incluindo+as+Horas+do+Saldo+Anterior+Valorizado+no+Espelho+de+Ponto)
