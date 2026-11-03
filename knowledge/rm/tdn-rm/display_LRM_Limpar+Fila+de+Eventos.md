---
content_hash: fd332cd1582de894c3e84e1ef10fd6e266bf66af2c6e4e53901719503e62e94f
fetched_at: '2026-06-29T00:10:07.955950+00:00'
page_id: '452719483'
product: rm
source: tdn-rm
title: Limpar Fila de Eventos
type: documentation
url: https://tdn.totvs.com/display/LRM/Limpar+Fila+de+Eventos
version: 2
---

Esse processo apaga todos registros existentes na fila de eventos independente do seu status. Pode ser usado quando a empresa necessitar alterar o tipo de ambiente de testes para produção, ou seja, quando precisar apagar todos os registros resultantes de testes, passando então a ter seu ambiente como produção.  
    
 **Atenção:**

1. Deverá ser selecionado quais os tipos de eventos que serão considerados na execução do processo.
2. Esse processo é IRREVERSÍVEL. Sendo assim é importante ter certeza da necessidade da sua execução.
3. Antes de "Limpar Fila Eventos " é  imprescindível ter executado o processo 'Atualizar Status Integração TAF' .
4. Caso o tipo de ambiente seja igual a "1-produção" e existir eventos na fila com status igual a 10-Aceito RET, não será possível concluir o processo "Limpar fila de Eventos"  e será exibida a seguinte mensagem para o usuário:

Foram encontrados eventos do eSocial já transmitidos para o RET (governo) nas coligadas:"XXX".  
 Os eventos dessas coligadas não foram excluídos.  
        
 Caso esteja em ambiente diferente do tipo "1-Produção", será possível concluir o processo "Limpar a fila de Eventos" .  
    
 Para ambos os casos será exibida a mensagem para o usuário:  
    
 ATENÇÃO!  
    
 Foram encontrados eventos do eSocial já integrados com o TAF nas coligadas: "XXX"   
                         Para manter a integridade das informações, após excluir os eventos no RM será necessário excluir    
                         também os eventos no TAF Confirma a exclusão?.
