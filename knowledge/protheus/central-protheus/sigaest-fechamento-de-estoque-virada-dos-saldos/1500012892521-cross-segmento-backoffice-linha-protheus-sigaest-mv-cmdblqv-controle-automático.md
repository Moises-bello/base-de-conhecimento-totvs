---
article_id: 1500012892521
category: SIGAEST - FECHAMENTO DE ESTOQUE (VIRADA DOS SALDOS)
content_hash: 3d28296bd4d970767af9c7e183474b9d0593cd90a9ffe300dc4b7b59c41aa38f
fetched_at: '2026-06-28T22:38:52.749896+00:00'
product: protheus
section_id: 1500001538921
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MV_CMDBLQV - Controle
  automático de bloqueio de movimentação durante o Custo Médio e Fechamento de Estoque
type: support-article
updated_at: '2024-06-07T11:33:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012892521-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-CMDBLQV-Controle-autom%C3%A1tico-de-bloqueio-de-movimenta%C3%A7%C3%A3o-durante-o-Custo-M%C3%A9dio-e-Fechamento-de-Estoque
---

**Dúvida**Como é utilizado e qual é a utilidade do parâmetro MV\_CMDBLQV?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Durante o processo de fechamento do estoque, ao executar o **Recálculo do Custo Médio** de forma **não exclusiva**, podem ocorrer movimentações no sistema que acabam por interferir ou distorcer o custo dos produtos. Neste cenário a alternativa para impedir movimentações no sistema que interfiram no cálculo do fechamento é solicitar ao administrador do sistema a configuração do parâmetro **MV\_DBLQMOV** com a data do fechamento pretendida.  
  
Com esta necessidade, para que este processo possa ocorrer de forma automática, foi implementada melhoria através da criação do parâmetro **MV\_CMDBLQV** para gravar a data de processamento do Recálculo do Custo Médio (informada no campo *"Data Limite Final ?"* da tela de parâmetros) no parâmetro **MV\_DBLQMOV** bloqueando novas movimentações durante e após o término do recálculo (garantindo assim integridade entre a data de execução do recálculo e a data da virada).  
Ao efetuar a **Virada dos Saldos** o sistema irá sugerir automaticamente a data da virada a partir do parâmetro **MV\_DBLQMOV** e bloquear a edição desta data pelo usuário, evitando desta forma erros durante o processo de realização da virada.

**Configuração do parâmetro**

No **Configurador (SIGACFG)**, acesse **Ambientes/Cadastros/Parâmetros (CFGX017)**.  
Crie o parâmetro com os dados abaixo conforme exemplo:

|  |  |
| --- | --- |
| **Campo** | **Conteúdo** |
| **Nome da Variável** | MV\_CMDBLQV |
| **Tipo** | Lógico |
| **Descrição** | Atualiza o parâmetro MV\_DBLQMOV com a data do recálculo do custo médio e sugere esta data na virada dos saldos. |
| **Valor Padrão** | .F. |

**OBS: Caso o cliente queira habilitar o conceito, basta já criar o parâmetro com conteúdo = .T.**

Configuração na prática:

![](https://tdn.engpro.totvs.com.br/download/attachments/585317091/MV_CMDBLQV.gif?version=1&modificationDate=1609963236773&api=v2)

**Exemplo de utilização**

No **Estoque e Custos (SIGAEST)**, acesse **Miscelânea/Cálculos/Custo Médio (MATA330)**.  
Informe a data desejada no campo *"Data Limite Final ?"* e confirme para executar o recálculo do custo médio.

![](https://tdn.engpro.totvs.com.br/download/attachments/585317091/MATA330.gif?version=1&modificationDate=1609965757760&api=v2)

Em seguida acesse:

- **Miscelânea/Fechar Períodos/Virada dos Saldos (MATA280);**  
- Informe as perguntas conforme desejado e clique em Ok;  
- Verifique que o campo *"Data Base para executar o fechamento:"* é sugerido com a mesma data informada no recálculo do custo médio e **fica desabilitado** **para** **alteração**;  
- Confirme para executar a virada dos saldos.

![](https://tdn.engpro.totvs.com.br/download/attachments/585317091/MATA280.gif?version=1&modificationDate=1609966988230&api=v2)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Fechamento de Estoque (Virada de Saldos)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538921-SIGAEST-FECHAMENTO-DE-ESTOQUE-VIRADA-DOS-SALDOS-)*

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614)
