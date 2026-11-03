---
article_id: 39237808461207
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: cfe11447bb5288e990d4031827e2240df465f6e5350e9107aa82af7e197d916f
fetched_at: '2026-06-28T22:40:32.596294+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - Contabilidade
  Gerencial - Sistema não permite ir para a próxima linha ou salvar os lançamentos
  na contabilização
type: support-article
updated_at: '2026-03-26T11:41:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39237808461207-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-Contabilidade-Gerencial-Sistema-n%C3%A3o-permite-ir-para-a-pr%C3%B3xima-linha-ou-salvar-os-lan%C3%A7amentos-na-contabiliza%C3%A7%C3%A3o
---

O sistema Protheus não permite avançar ou salvar lançamentos contábeis devido a inconsistências nos registros, como divergências entre débito e crédito. Para identificar o erro, é necessário ativar os parâmetros MV\_CT105MS e MV\_ALTLCTO no módulo Configurador, permitindo que o sistema exiba mensagens detalhadas para correção e continuidade do processo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39237799354391) Tempo aproximado para leitura: 00:10 min  
  
**Dúvida**  
Ao realizar uma contabilização, o sistema não está permitindo ir para a próxima linha ou salvar os lançamentos.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - Contabilidade Gerencial - A partir da versão 12.

**Solução**  
O sistema não permite ir para a próxima linha ou salvar os lançamentos pois há alguma inconsistência ou falta de dados no registro contábil (como divergencia entre dbito e crédito, entidade bloqueade e etc.),o que bloqueia a continuidade do processo.

Para que o sistema informe detalhadamente qual é a inconsistência e permita a correção, é necessário ativar o parâmetro **MV\_CT105MS** e **MV\_ALTLCTO**. Desta forma, será apresentado em tela um *help* indicando o motivo da falha no registro, possibilitando a alteração do que está incorreto para a posterior gravação.

*Observação: O sistema aciona a validação do parâmetro MV\_CT105MS apenas quando o parâmetro **MV\_ALTLCTO** está com o conteúdo igual a "S".*

1. Acesse o módulo Configurador (SIGACFG).
2. Siga pelo menu **Ambiente > Cadastros > Parâmetros**.
3. Localize o parâmetro **MV\_CT105MS** e clique em Editar.
4. Altere o conteúdo do parâmetro para **"S"** (Mostra mensagem).
5. Localize o parâmetro **MV\_ALTLCTO** e certifique-se de que o conteúdo também seja **"S"**.
6. Confirme e salve as alterações realizadas.
7. Saia do sistema, entre na rotina de contabilização novamente e execute o processo. Ao encontrar um erro, a tela exibirá a inconsistência específica da linha.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39237799355543)

**Saiba Mais**  
[Contabilização não valida a linha do lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059273293-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA105-Contabiliza%C3%A7%C3%A3o-Off-Line-n%C3%A3o-valida-a-linha-do-lan%C3%A7amento)
