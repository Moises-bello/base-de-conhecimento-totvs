---
article_id: 360048044333
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: be5995aff4ca615c9fc55b5f75367942490d5918be1c842cd464ae5821d25e2c
fetched_at: '2026-06-28T22:42:43.464607+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Integração TOTVS MES - Estrutura de
  Produtos
type: support-article
updated_at: '2022-05-10T16:12:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048044333-Manufatura-Linha-Protheus-SIGAPCP-Integra%C3%A7%C3%A3o-TOTVS-MES-Estrutura-de-Produtos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min**  
**Ocorrência**  
Ao efetuar a integração do **MATA200/PCPA200 - Cadastro de Estrutura** via **TOTVS MES**, apresenta mensagens de inconsistência.  
   
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Integração e mensagens de inconsistências que podem ocorrer na integração **TOTVS MES**.  
  
**Solução**  
Na **Engenharia** o **MATA200/PCPA200** pode enviar dados via **TOTVS MES**, em toda a inclusão, alteração e exclusão de estrutura.  
  
**Sincronização**: Permite realizar a sincronização dos dados entre o **Protheus** e o **PC-Factory**. Poderá enviar os dados dos **Produtos**, **Local de Estoque**, **Recurso**, **Máquina**, **Roteiro**, **Estrutura**, **Endereço**, **Saldo em Estoque** e **Ordem de Produção**.  
  
 **PCPA110 - Pendências**: Rotina para reenviar as mensagens não enviadas ao Sistema **PC-Factory**, sejam elas pendências ou erro. A rotina também possibilita consultar as mensagens enviadas, **LOG de envio.**Quando incluir, alterar ou excluir dados do **MATA637 - Operações x Componente**, deverá reenviar a mensagem de estrutura.  
  
Mensagens durante a integração:

1. **Atenção! Ocorreram erros na integração com o TOTVS MES. Erro: XXXX. Deseja incluir/alterar/excluir a estrutura no protheus e gerar pendência para integração?****Resposta:** Caso ocorra algum erro no envio das informações, será apresentado a pergunta acima. Se o cliente responder sim, poderá avaliar a mensagem e reprocessar depois através do **PCPA110** , mas a gravação do registro que está sendo incluído/alterado/excluído será efetivado no **PCPA200/MATA200**.
2. **Não foi possível realizar a integração com o TOTVS MES para o produto '"XXX"'. Foi gerada uma pendência de integração para este produto.****Resposta:** Ocorreu algum erro na tentativa de integração. No **PCPA110**, terá maiores detalhes sobre a ocorrência. As mensagens que podem ocorrer, estão em anexo neste documento.
3. **Não existe caminho de WebService cadastrado. Verifique os parâmetros da integração.****Resposta:** Deve-se informar um **webservice** válido no **PCPA109 - Parâmetros** no campo **Caminho**.    
   **Caminho**: Indica o caminho do **WebService** do **PC-Factory**. Após o caminho, tem um botão **testar** para verificar se **webservice** está **ativo**.
4. **Não foi possível realizar a conexão com o WebService do TOTVS MES. Favor verificar as configurações de conexão. Erro:****Resposta:** Estas mensagens podem ocorrer quando o serviço de **webservice** não está no ar.
5. **O link é um wsdl válido. Porém não contém os métodos utilizados para integração com o TOTVS MES. Favor verificar as configurações de conexão.****Resposta:** Não foi possível identificar na mensagem qual é a operação que deverá ser realizada, inclusão/alteração/modificação/exclusão.
6. **Não conseguiu setar a operação XXXX. Erro: XXX**  
   **Resposta:** Não foi encontrada a *tag* **Event** no **XML** gerado/enviado
7. **Não foi possível utilizar o XML. Erro:****Resposta:** O **XML** informado está com o formato inválido ou com algum erro nas suas *tag´s*. Deverá ser verificado se o **xml** está em um formato válido e com as *tag´s* do **XML** sendo abertas e fechadas corretamente.
8. **Não foi possível realizar o parse do XML de retorno do TOTVS MES.****Resposta:** O endereço da *tag* **TOTVSMessage** está inválido.
9. **O diretório '" XXX "' é inválido.****Resposta:** Os diretórios informados nos campos: **Enviados** e **Pendência** do **PCPA109** estão incorretos ou não existem.  
   Campos do **PCPA109** que devem ser revisados:  
   - **Gera XML** - Ao selecionar esse campo, irá gerar os **XML** das mensagens trocadas. Se não estiver selecionado, será gravado apenas em tabelas. A geração dos arquivos não é obrigatória. Serve como uma ferramenta útil para encontrar problemas. O envio sempre será feito com base do que estiver registrado nas tabelas;  
   - **Enviados** - Diretório onde serão salvos os **XMLs** enviados com sucesso ao **PC-Factory**;- **Pendência** - Diretório onde serão salvos os **XMLs** que não foram enviados ao **PC-Factory**.
10. **Erro ao criar o arquivo XML no diretório '" XXX "'. Erro:****Resposta:** Verificar se o usuário possui permissão de gravação nos diretórios informados no **PCPA109** ou se o nome do diretório possui algum caracter especial.
11. **Não é possível enviar Xml com caracteres especiais. Por favor, revise o cadastro do Produto XXXX****Resposta:** O cadastro de estrutura no **MATA200/PCPA200** possui caracteres especiais e devem ser retirados.  
      
    Abaixo, há alguns exemplos de caracteres que podem causar problemas no envio da mensagem de **Estrutura** para o **Totvs MES** e a recomendação é retirá-los do cadastro:
    * €
    * ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069254134/mceclip0.png)
    * Ž
    * ü
    * ì
    * Å
    * É
    * ¥
    * (
    * )

**Saiba mais  
Referente ao item 4**:  segue documentações complementares:  [URLs acessadas pela TWsdlManager](https://tdninterno.totvs.com/display/tec/URLs+acessadas+pela+TWsdlManager) e [TWsdlManager:ParseURL](https://tdninterno.totvs.com/display/tec/TWsdlManager%3AParseURL)**Referente ao item 11**: Para maiores informações sobre os caracteres acesse a documentação: [EncodeUTF8](https://tdn.totvs.com/display/tec/EncodeUTF8)Informações mais detalhadas sobre a integração **TOTVS MES**, podem ser encontradas no **Manual**: [Integração PCP Protheus x PPI-Multitask](https://tdn.totvs.com.br/pages/releaseview.action?pageId=208340274)
