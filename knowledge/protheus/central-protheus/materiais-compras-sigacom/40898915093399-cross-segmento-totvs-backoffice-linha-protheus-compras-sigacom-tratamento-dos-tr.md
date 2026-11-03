---
article_id: 40898915093399
category: Materiais - Compras (SIGACOM)
content_hash: 3c83357c021afd08cf279a62960b5882d0f6be9728c81c3658752dff72f6b055
fetched_at: '2026-06-28T22:41:07.322991+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras (SIGACOM) - Tratamento
  dos tributos CBS e IBS no Novo Fluxo de Compras (NFC)
type: support-article
updated_at: '2026-06-02T12:01:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40898915093399-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Compras-SIGACOM-Tratamento-dos-tributos-CBS-e-IBS-no-Novo-Fluxo-de-Compras-NFC
---

### Dúvida

Como visualizar a incidência e os cálculos dos novos impostos CBS Federal (Contribuição sobre Bens e Serviços) e IBS Estadual/Municipal (Imposto sobre Bens e Serviços) na tela de análise e edição de cotação dentro do Novo Fluxo de Compras (NFC)?

### Ambiente

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras (SIGACOM) - Protheus Release 12.1.2310 

### Solução

Foram realizados ajustes no sistema para permitir que o Novo Fluxo de Compras (NFC) passe a considerar e exibir os impostos previamente configurados no Configurador de Tributos (FISA170). A implementação contempla a exibição detalhada desses valores em tela de maneira dinâmica e otimizada, garantindo a integridade dos dados no banco de dados.

* **Cálculo em Memória:** Na tela de edição da cotação, ao acionar a opção para calcular impostos, os valores do CBS e IBS serão processados e exibidos diretamente na aba Tributos Genéricos. O sistema mantém essas informações em memória temporária para evitar a gravação de registros desnecessários.
* **Gravação dos Dados:** A persistência de dados na tabela F2D (Tributos Genéricos Calculados) e o preenchimento do campo C8\_IDTRIB ocorrerão exclusivamente no momento em que a cotação for salva pelo usuário.

![](https://tdn.totvs.com/download/attachments/981002683/image-2025-8-29_14-47-0.png?version=1&modificationDate=1756489621010&api=v2)

* **Exibição Dinâmica de Valores:** Os novos campos CBS Federal, IBS Estadual e IBS Municipal foram inseridos na área de Impostos Totais na tela de edição. A exibição dessas informações em formato de card ou colunas é dinâmica; ou seja, se o imposto possuir valor zerado (R$ 0,00), ele ficará oculto para otimização do espaço em tela e facilidade de leitura.
* **Análise da Cotação:** A aba Impostos apresenta um grid estruturado contendo o sequencial do item, o código do produto e o detalhamento dos tributos correspondentes a cada item avaliado.

![](https://tdn.totvs.com/download/attachments/981002683/image-2025-8-29_14-49-31.png?version=1&modificationDate=1756489771313&api=v2)

* **Mercado Internacional (MI):** Para operações voltadas ao Mercado Internacional, a aba de tributos genéricos não será exibida no detalhamento da cotação, uma vez que se trata de uma tributação exclusiva do cenário brasileiro. No card de impostos, a estrutura fixa é substituída pela nomenclatura geral "Imposto", preenchendo os campos dinâmicos nativos do MI (C8\_VALIMP1 a C8\_VALIMPZ).
* **Regras de Acréscimo e Abatimento:** Parametrizações do Configurador de Tributos que determinam se o imposto deve ser acrescido ou abatido do valor total só surtirão efeito final na geração do Documento de Entrada e nas Duplicatas. Nas rotinas anteriores, como Cotação e Análise de Cotação, essas regras não alteram os montantes exibidos. Na rotina de Pedido de Compra (MATA120), o sistema exibe visualmente uma prévia somando ou abatendo o imposto no campo Total em tela, porém, ao confirmar o registro, o campo total do pedido será salvo sem considerar tais variações de abatimento ou acréscimo, mantendo o padrão legado do sistema.

### Passos

1. Certifique-se de que as regras tributárias para o CBS e IBS estejam devidamente criadas na rotina Configurador de Tributos (FISA170).
2. Acesse a rotina do Novo Fluxo de Compras (NFC) e abra a tela de edição de uma cotação aplicável.
3. Clique na opção para calcular os impostos para processar a simulação em memória.
4. Navegue até a aba Tributos Genéricos para visualizar os valores e alíquotas calculados.
5. Avalie os valores somados nos campos de impostos totais (CBS Federal, IBS Estadual e IBS Municipal).
6. Salve a cotação para que o sistema execute a gravação definitiva na tabela F2D e no campo C8\_IDTRIB.
7. Na tela de análise da cotação, verifique as informações consolidadas por item e por produto diretamente no grid da aba de impostos.

### Saiba Mais

* [Novo Fluxo de Compras: Guia de Referência - Gestão de Compras - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=981002683)
* [CFGTRIB - Configurador de Tributos - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=981002683)
