---
article_id: 40822072165655
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 98730a1d1f16cc071ebe7c3edc1fa3fcdf77e8a91d858e82777cc3f889e372f3
fetched_at: '2026-06-28T22:38:58.489658+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Erro FWFormViewStruct
  SETPROPERTY Campo D2_(XPTO)não encontrado
type: support-article
updated_at: '2026-06-01T12:45:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40822072165655-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Erro-FWFormViewStruct-SETPROPERTY-Campo-D2-XPTO-n%C3%A3o-encontrado
---

Ao tentar incluir uma nota de débito (MATA600) no TOTVS Protheus, pode ocorrer erro relacionado a campos do dicionário de dados (ex.: D2\_LOCALIZ) com restrição de uso em módulos incorretos. A solução é acessar o Configurador (SIGACFG), editar o campo no Dicionário de Dados, ajustar a restrição de módulos para o ambiente correto, salvar e atualizar o dicionário, permitindo o funcionamento da tela.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40822065512471) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**  
Ao tentar incluir uma nota de débito (MATA600), o sistema apresenta o seguinte erro: "erro no parâmetro FWFormViewStruct: O erro no método SETPROPERTY: Campo D2\_LOCALIZ não encontrado. on FWFORMVIEWSTRUCT:SETPROPERTY". Este mesmo incidente pode ocorrer indicando outros campos do dicionário de dados pertinentes à tabela SD2, sendo os mais recorrentes os campos D2\_LOCALIZ, D2\_LOTECTL e D2\_NUMSERI

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões

**Causa**  
A ocorrência se deve ao fato de que o campo referenciado na mensagem de erro (como o D2\_LOCALIZ) está com sua utilização restrita no Dicionário de Dados (SX3), associado especificamente a módulos que não correspondem ao uso do processo em questão (por exemplo, definido apenas para o SIGALOJA), ou não estar marcado como usado no configurador. Essa limitação de módulos afeta diretamente a composição de uso do campo na base (X3\_USADO), fazendo com que a tela MVC não localize a propriedade durante a montagem da interface (FWFormViewStruct).

**Solução**

Para solucionar a ocorrência e permitir a abertura da tela, siga os passos abaixo:

1. Acesse o módulo Configurador (SIGACFG).
2. Siga pelo menu em Base de Dados > Dicionário > Bases de Dados.
3. Posicione em "Dicionário de Dados" e clique na lupa para pesquisar o campo mencionado no erro (exemplo: D2\_LOCALIZ, D2\_LOTECTL ou D2\_NUMSERI).
4. Clique em Editar.
5. Acesse a aba "Módulos".
6. Remova a restrição, modificando o campo para todos os módulos ou marcando as caixas de seleção dos módulos específicos utilizados em seu ambiente.
7. Confirme a alteração, salve e proceda com a Atualização do Dicionário de Dados.
8. Acesse novamente a rotina afetada e confirme que a tela de entrada de dados voltará a funcionar normalmente.

Segue em anexo a SX3 da SD2 dos campos D2\_LOTECTL, D2\_LOCALIZ e D2\_NUMSERI com a estrutura padrão para validação e comparação. 

**OBS**: Os dados são para auxílio e comparação em relação ao ambiente com o cenário. Caso queira utilizar o exemplo padrão, realizar um backup e avaliar se possui diferença nos tamanhos, formatos e pictures dos campos para não causar impactos no ambiente.

 

**Saiba mais**:

[*Como configurar a rotina MATA600 Notas de Débito?*](https://tdn.totvs.com/x/MZ5qP)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Nota de Débito do tipo 7 Perda em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40653605488663)

[*Notas de Débito (MATA600) - ExecAuto*](https://tdn.totvs.com/x/4cg1Pg)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
