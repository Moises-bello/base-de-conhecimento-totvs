---
article_id: 360047350894
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: c5ae578a18e2b2b4b7d0e96fb59256fb19d5aabd380a37023efe2c2d21a931d3
fetched_at: '2026-06-28T22:42:43.446773+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Integração TOTVS MES - Cadastro do
  Produto
type: support-article
updated_at: '2022-05-10T16:09:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047350894-Manufatura-Linha-Protheus-SIGAPCP-Integra%C3%A7%C3%A3o-TOTVS-MES-Cadastro-do-Produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:30 min**  
**Ocorrência**  
No módulo do **PCP -****Planejamento e Controle da Produçã**o ao efetuar a integração do **MATA010 - Cadastro de Produto** via **TOTVS MES**, apresenta mensagens de inconsistências.  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Essas mensagens podem ocorrer, por configuração incorreta do **WebService** e/ou no **Cadastro de Produto**.  
   
**Solução**  
**Produto:** A inclusão, alteração ou exclusão de um produto no programa **MATA010** vai gerar integração com **PC-Factory** caso a integração esteja ativa no cadastro do programa **PCPA109 - Parâmetros**.  
Caso ocorra erro no envio do registro, uma mensagem será exibida e será enviado uma pendência de envio no programa de **Gerenciamento de Pendências de Integração**, o **PCPA110 - Pendências**, e a atualização para o **PC-Factory** deverá ser realizada por meio do **PCPA110**.  
  
**Mensagens de inconsistência:**

1. **Não existe caminho de WebService cadastrado. Verifique os parâmetros da integração.**  
   **Resposta:** Deve-se informar um **webservice** válido no **PCPA109** no campo **Caminho**.   
   **Caminho:** Indica o caminho do **WebService** do **PC-Factory**. Após o caminho, terá um botão testar para verificar se **webservice** está ativo.
2. **Não foi possível realizar a conexão com o WebService do TOTVS MES. Favor verificar as configurações de conexão. Erro:**   
   **Resposta:** Estas mensagens podem ocorrer quando o serviço de **webservice** não está no ar.
3. **O link é um wsdl válido. Porém não contém os métodos utilizados para integração com o TOTVS MES**. **Favor verificar as configurações de conexão.**  
   **Resposta:** Não foi possível identificar na mensagem qual é a operação que deverá ser realizada, inclusão/alteração/modificação/exclusão;
4. **Não conseguiu setar a operação XXXX. Erro: XXX****Resposta:** Não foi encontrada a *tag* **Event** no **XML** gerado/enviado;
5. **Não foi possível utilizar o XML. Erro:**   
   **Resposta:** O **XML** informado está com o formato inválido ou com algum erro nas suas *tag´s*. Deverá ser verificado se o **XML** está em um formato válido e com as *tag´s* do **XML** sendo abertas e fechadas corretamente.
6. **Não foi possível realizar o parse do XML de retorno do TOTVS MES.****Resposta:** O endereço da *tag* **TOTVSMessage** está inválido.
7. **O diretório '" XXX "' é inválido.****Resposta:** Os diretórios informados nos campos: Enviados e Pendência do **PCPA109** estão incorretos ou não existem.  
   Campos do **PCPA109** que devem ser revisados:  
   **- Gera XML** - Ao selecionar esse campo, irá gerar os **XML** das mensagens trocadas. Se não estiver selecionado, será gravado apenas em tabelas. A geração dos arquivos não é obrigatória. Serve como uma ferramenta útil para encontrar problemas. O envio sempre será feito com base do que estiver registrado nas tabelas;  
   **- Enviados** - Diretório onde serão salvos os **XMLs** enviados com sucesso ao **PC-Factory**;  
   **-** **Pendência** - Diretório onde serão salvos os **XMLs** que não foram enviados ao **PC-Factory.**
8. **Erro ao criar o arquivo XML no diretório '" XXX "'. Erro:****Resposta:** Verificar se o usuário possui permissão de gravação nos diretórios informados no **PCPA109** ou se o nome do diretório possui algum caracter especial.
9. **Não é possível enviar XML com caracteres especiais. Por favor, revise o cadastro do Produto XXXX****Resposta:** O cadastro do produto no **MATA010** possui caracteres especiais e devem ser retirados.  
     
   Abaixo, há alguns exemplos de caracteres que podem causar problemas no envio da mensagem de **Produto** para o **Totvs MES** e a recomendação é retirá-los do cadastro:
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

**Saiba mais**1. **Ponto de Entrada:** para o **Cadastro de Produto** o ponto de entrada **PCPADDTAGS** permite incluir *tags* específicas nas mensagens padrões **TOTVS**. Está habilitado para o cadastro de item **MATA010**. Detalhes em: [PCPADDTAGS - Adicionar informações XML Integração TOTVS MES](https://tdn.totvs.com.br/pages/viewpage.action?pageId=268571501).2. **Referente ao item** **2**: segue documentações complementares: [URLs acessadas pela TWsdlManager](https://tdninterno.totvs.com/display/tec/URLs+acessadas+pela+TWsdlManager) e [TWsdlManager:ParseURL](https://tdninterno.totvs.com/display/tec/TWsdlManager%3AParseURL)  
  
3. **Referente ao item 9**: Para maiores informações sobre os caracteres acesse a documentação: [EncodeUTF8](https://tdn.totvs.com/display/tec/EncodeUTF8)4. Informações mais detalhadas sobre a integração **TOTVS MÊS**, podem ser encontradas no **Manual**: [Integração PCP Protheus x PPI-Multitask](https://tdn.totvs.com.br/pages/releaseview.action?pageId=208340274)
