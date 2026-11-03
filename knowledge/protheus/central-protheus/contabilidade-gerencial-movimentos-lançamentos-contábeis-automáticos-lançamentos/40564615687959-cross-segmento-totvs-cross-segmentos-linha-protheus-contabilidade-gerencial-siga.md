---
article_id: 40564615687959
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: eaaf6ac5b7b4e130b72fd63c884293e8080b9926a70bb974c7e6b3cd43f1a0b1
fetched_at: '2026-06-28T22:40:32.619969+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - TOTVS Cross Segmentos (Linha Protheus) - Contabilidade Gerencial
  (SIGACTB) - Como evitar a geração de mais de uma linha de histórico (continuação
  de histórico) em integrações de módulos
type: support-article
updated_at: '2026-06-01T20:39:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40564615687959-Cross-Segmento-TOTVS-Cross-Segmentos-Linha-Protheus-Contabilidade-Gerencial-SIGACTB-Como-evitar-a-gera%C3%A7%C3%A3o-de-mais-de-uma-linha-de-hist%C3%B3rico-continua%C3%A7%C3%A3o-de-hist%C3%B3rico-em-integra%C3%A7%C3%B5es-de-m%C3%B3dulos
---

Para evitar que a integração off-line com a Contabilidade Gerencial crie uma segunda linha ao ultrapassar o limite do campo CT2\_HIST, desative o parâmetro MV\_CT5HIST no módulo Configurador (definindo-o como .F.) e garanta que o campo CTK\_HIST tenha tamanho igual ou superior ao CT2\_HIST. Após ajustes, salve e atualize o dicionário de dados.

**Dúvida**   
Como configurar o sistema para que, durante a integração off-line de módulos com a Contabilidade Gerencial, caso o histórico ultrapasse o limite de caracteres do campo histórico (CT2\_HIST), a informação seja apenas truncada e não gere uma segunda linha (linha de continuação de histórico Tipo 4)?

**Ambiente**   
Cross Segmento - TOTVS Cross Segmentos (Linha Protheus) - Contabilidade Gerencial (SIGACTB) - Protheus 12.1.2410 

**Solução**   
Em lançamentos contábeis realizados por meio de integração de módulos, o sistema avalia a necessidade de quebra de linha comparando o tamanho dos campos histórico (CT2\_HIS) (Lançamentos Contábeis) e histórico (CTK\_HIST) (Arquivo de Contra-Prova). Para garantir que o Protheus não crie o Lançamento Tipo 4 (continuação), é necessário manter o parâmetro de quebra de histórico desativado e certificar-se de que o campo do arquivo de contra-prova possua tamanho igual ou maior que o campo de lançamento.

**Passos**

1. Acesse o módulo **Configurador (SIGACFG)**, vá em **Ambiente > Cadastros > Parâmetros** e localize o parâmetro **MV\_CT5HIST**.
2. Altere o valor do parâmetro **MV\_CT5HIST** para **.F.** (Falso) para desabilitar o controle padrão de corte de histórico.
3. Acesse o **Dicionário de Dados** no Configurador e verifique as definições de tamanho dos campos **CT2\_HIST** (Tabela CT2) e **CTK\_HIST** (Tabela CTK).
4. Garanta que o tamanho do campo **CTK\_HIST** seja **igual ou superior** ao tamanho configurado no campo **CT2\_HIST**.
5. Salve as alterações e atualize o dicionário de dados.

**Saiba Mais**  
[Tamanho do histórico no lançamento contábil](https://www.google.com/search?q=https://tdn.totvs.com/pages/releaseview.action%3FpageId%3D606649086)
