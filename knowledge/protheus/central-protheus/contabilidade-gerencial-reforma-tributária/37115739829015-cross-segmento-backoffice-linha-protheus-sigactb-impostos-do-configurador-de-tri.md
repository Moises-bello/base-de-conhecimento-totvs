---
article_id: 37115739829015
category: Contabilidade gerencial - Reforma Tributária
content_hash: 0b19c5409ffa3a477515f25d01c1cf11604c6c4d1dc11e7d371063e3f0995901
fetched_at: '2026-06-28T22:40:29.727514+00:00'
product: protheus
section_id: 37095816599831
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Impostos do Configurador
  de Tributos no Conciliador backoffice
type: support-article
updated_at: '2026-01-02T17:08:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37115739829015-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Impostos-do-Configurador-de-Tributos-no-Conciliador-backoffice
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37115756828055) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como visualizar e utilizar os impostos calculados pelo Configurador de Tributos dentro da rotina CTBA940 - Conciliador Backoffice?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade gerencial - A partir da versão 12.1.33  
  
**Solução**  
Nas conciliações que envolvem as tabelas de documentos de entrada (**SD1**) e saída (**SD2**), o Protheus permite adicionar colunas específicas para os impostos gerados via Configurador de Tributos. Essa funcionalidade facilita a conferência e identificação de valores tributários por registro diretamente na tela de conciliação.

Para o recurso funcionar corretamente, é necessário que o dicionário de dados esteja atualizado com o campo **QLB\_CFGTRB** na tabela Conciliador Backoffice- Chaves (**QLB)**.  
  
  
**Passos a passo:**

1. **Selecionando Tributos na Configuração**

* Ao **Incluir** ou **Alterar** uma configuração de conciliação (Setup), acesse a etapa **Campos**.
* Se a tabela selecionada for **SD1** ou **SD2**, o botão **"Configurador de Tributos"** ficará visível.
* Clique no botão para abrir a lista de tributos gerados na tabela **F2D**.

![](https://tdn.totvs.com/download/attachments/1006410757/trib01.gif?version=2&modificationDate=1761774018480&api=v2)

* Os tributos só aparecem se houver registros calculados na F2D para a combinação de tabelas da conciliação. Por exemplo: se a configuração de conciliação for **SD1 x CT2**, estarão disponíveis apenas os impostos que já tiverem sido **calculados na F2D** para essa combinação.
* Selecione as regras de impostos desejadas
* Se houver mais de uma regra para o mesmo tributo, os valores serão somados em uma única coluna.
* Clique em **"Salvar Alterações"** e grave a configuração.

![](https://tdn.totvs.com/download/attachments/1006410757/trib02.gif?version=2&modificationDate=1761774240970&api=v2)

2. **Visualização dos tributos na conciliação**

* Ao executar a conciliação, os impostos selecionados aparecerão nas **últimas colunas** da grade.
* O nome da coluna será identificado pelo prefixo **(T)** seguido pelo nome do tributo.

![](https://tdn.totvs.com/download/attachments/1006410757/trib03.gif?version=1&modificationDate=1761827097807&api=v2)

 3. **Regra de match**

* Os valores dos tributos podem ser utilizados para criar **Regras de Match**.

![](https://tdn.totvs.com/download/attachments/1006410757/chrome_g0z2rrHLPG.gif?version=2&modificationDate=1761828762210&api=v2)

Exemplo: É possível configurar um match onde o valor do tributo PIS deve ser igual ao campo CT2\_VALOR.

![](https://tdn.totvs.com/download/attachments/1006410757/chrome_HZRr7P1ITy.gif?version=1&modificationDate=1761828777677&api=v2)

4. **Totalizadores**

* Os tributos também podem ser inseridos nos **Totalizadores** da conciliação, permitindo a comparação de somatórios e verificação de divergências diretamente.

![](https://tdn.totvs.com/download/attachments/1006410757/trib04.gif?version=1&modificationDate=1761827589127&api=v2)

**Videos** ***How To*****:**

|  |  |
| --- | --- |
|  |  |

**Saiba Mais**

[TDN: Impostos do Configurador de Tributos na Conciliação](https://tdn.totvs.com/pages/releaseview.action?pageId=1006410757)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Contabilização com Base na Sigla do Tributo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37100272710039-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Contabiliza%C3%A7%C3%A3o-com-Base-na-Sigla-do-Tributo)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Contabilização com Base na Classificação do Tributo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37097599152663-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Contabiliza%C3%A7%C3%A3o-com-Base-na-Classifica%C3%A7%C3%A3o-do-Tributo)
