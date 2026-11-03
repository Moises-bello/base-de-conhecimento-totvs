---
content_hash: f14a90f7c1fd33f3aa2014efe7fb553ca9842da8cb849d5ae183086c96b6a30a
fetched_at: '2026-06-29T00:10:01.333128+00:00'
page_id: '452718688'
product: rm
source: tdn-rm
title: Copiar Evento entre Coligadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Copiar+Evento+entre+Coligadas
version: 2
---

Este assistente irá auxiliá-lo na cópia de registro(s) entre as coligada(s) do sistema.   
 Para utilizar o assistente clique no botão Avançar.

**Parâmetros da cópia**

Na janela de Parâmetros da cópia o sistema lista todas as coligadas disponíveis na base de dados para se fazer à cópia de registro. Selecione a coligada ou as coligadas que deseja fazer a cópia e clique no botão Avançar.

**Observações**  
 A coligada não ficará disponível caso o usuário não tenha permissão de incluir eventos na coligada destino.  
 Não é possível realizar a cópia de informações se na coligada de destino não existir um campo para tal informação.

**Exemplo**

Ao tentar copiar um evento calculado por fórmula e essa fórmula não estiver cadastrada na coligada destino o evento não será copiado.  
 Quando este fato ocorrer você tem duas opções para realizar a cópia:

1) excluir a fórmula associada ao evento, salvar a edição e repetir o processo de cópia de registros;

2) acessar a outra coligada(coligada destino do evento), cadastrar a fórmula com mesmo código da coligada origem e repetir o processo de cópia de registros.

**Substitui registros no destino se eles já existirem**

Marque esta opção quando já existir o evento na coligada de destino e deseja alterar seus dados pelos dados do evento da coligada de origem. Caso contrário o sistema manterá os dados do evento na coligada de destino.

Concluindo o Assistente de Cópia de Registros entre Coligadas

Para fazer a cópia de evento entre as coligadas clique no botão "Concluir".
