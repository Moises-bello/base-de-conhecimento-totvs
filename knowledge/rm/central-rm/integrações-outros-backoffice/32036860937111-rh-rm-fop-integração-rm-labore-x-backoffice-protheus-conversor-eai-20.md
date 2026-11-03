---
article_id: 32036860937111
category: Integrações Outros BackOffice
content_hash: f46969d759e517de9a44009d4b7b4b1cbd9e27796b96be3652ff667049699f83
fetched_at: '2026-06-28T22:46:42.104218+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: 'RH - RM - FOP - Integração RM Labore x BackOffice Protheus: Conversor EAI
  2.0'
type: support-article
updated_at: '2025-05-12T15:20:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32036860937111-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Conversor-EAI-2-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32036869116951) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como realizar a conversão do EAI 1.0 para o 2.0?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para converter a integração EAI 1.0 em EAI 2.0, realize os seguintes passos:  
1. Acesse o menu **Integração | Mensagem Única | Conversor EAI 2.0**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32036860917783)

2. Informe o endereço WSDL e REST do Protheus (Obrigatoriamente precisa existir os dois serviços e o APPSERVER iniciado) e faça a validação  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32036860918423)

3. Certifique-se que já exista o DE/PARA cadastrado para a tabela GCOLIGADA mapeando a coligada com o Grupo de Empresa do Protheus.

4. Faça a validação do compartilhamento de tabelas, a coluna **"Compartilhamento Protheus Permitido"** **não deve** apresentar erros. Caso apareça algum erro, clique sobre ele e siga as instruções para corrigir.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32036860919191)

5. No ambiente exemplo, a validação por Empresa não retornou nenhum erro (somente aviso e diagnóstico não implementado, que é permitido para o avanço), então poderá ser feita a validação pelo item desejado.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32036860919703)

6. O adapter WHOIS não é implementado nessa integração, poderá ignorar a mensagem.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32036860920343)

7. Desmarque importar Fila de Mensagens, clique no ícone para edição do Source Application e informe o ALIAS do Protheus nesse campo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32036869120663)

8. Se aparecer o erro:  
*“Existem transações cadastradas. As novas tabelas do EAI devem estar vazias para a correta execução desse processo!”*  
Será necessário limpar as tabelas manualmente no banco de dados RM. Utilize os comandos indicados para isso:![](https://centraldeatendimento.totvs.com/hc/article_attachments/32036869121687)

```
Tabela em Mensagem Única | Transformações  
DELETE from GEAITRANSACAOVERSAO
```

```
Tabela em Mensagem Única | Integração | Anexos | Mapeamento de Entidades  
DELETE from GEAITRANSACAO
```

9. Após realizar a limpeza das tabelas, o processo será concluído com êxito:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32036869122199)

10. Feito o procedimento, acesse novamente o módulo INTEGRAÇÃO onde será apresentada a aba EAI 2.0 para executar o configurador.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32036869122455)

**Saiba mais**[RM - FOP - Integração RM Labore x BackOffice Protheus Configurador EAI 2.0](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4576020312087-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Configurador-EAI-2-0)
