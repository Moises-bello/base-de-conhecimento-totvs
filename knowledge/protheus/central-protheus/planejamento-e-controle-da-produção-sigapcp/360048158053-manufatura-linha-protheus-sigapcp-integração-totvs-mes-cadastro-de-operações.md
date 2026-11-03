---
article_id: 360048158053
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 71f1ed31b32bc8bbb66d6584882cb65b072fa6f9bd163eb8e79ec11a9f92c568
fetched_at: '2026-06-28T22:42:43.435961+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Integração TOTVS MES - Cadastro de
  Operações
type: support-article
updated_at: '2022-05-10T16:08:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048158053-Manufatura-Linha-Protheus-SIGAPCP-Integra%C3%A7%C3%A3o-TOTVS-MES-Cadastro-de-Opera%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min**  
**Ocorrência**  
Ao efetuar a integração do**MATA632/PCPA124 - Cadastro de Operações** via **TOTVS MES**, apresenta mensagens de inconsistência.  
   
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
   
**Causa**Essas mensagens podem ocorrer, por configuração incorreta do **WebService** e ou no **Cadastro de Operações**.  
  
 **Solução**  
O envio das informações via **TOTVS MES** podem ser realizadas através da **Manutenção** das operações **MATA632** ou **PCPA124**, toda vez que houver inclusão, alteração e exclusão.   
O **PCPA110 - Pendências** pode reenviar as mensagens não enviadas ao Sistema **PC-Factory**, sejam elas pendências ou erro. A rotina também possibilita consultar as mensagens enviadas, **LOG de envio**.  
  
Algumas observações referentes a mensagem de envio do cadastro de operações:

* A *tag* **ActivityType** **- Tipo Operação** será gerada com o valor fixo **1**;
* A *tag* **UnitTimeType - Tipo Unidade Tempo** será gerada com o valor fixo **1**;
* Obrigatório informar as *tags* **InitialDate** e **FinalDate**. Cadastrada no **MATA632** ou **PCPA124**.
* A *tag* **ListOfPertOrders** não será gerada para o **Protheus**;
* Na exclusão de um roteiro, não deverá excluir se existir integridade com a rotina de **MATA637 - Operações x Componente**. Neste caso não necessita enviar nenhuma mensagem ao **PC-Factory**;
* Quando incluir, alterar ou excluir dados do **MATA637**, deverá reenviar a mensagem de estrutura, **ItemStructure**.

Quando houver alteração/exclusão nas operações e optar por atualizar as ordens de produção que utilizam aquele roteiro, a mensagem da **Ordem de Produção** - **ProductionOrder** também será enviada via **Totvs MES**.  
  
**Mensagens de inconsistência:**

1. **Não existe caminho de WebService cadastrado. Verifique os parâmetros da integração.****Resposta:** Deve-se informar um **webservice** válido no **PCPA109 - Parâmetros** no campo **Caminho**.   
   **Caminho:** Indica o caminho do **WebService** do **PC-Factory**. Após o caminho, terá um botão **testar** para verificar se **webservice** está ativo.
2. **Não foi possível realizar a conexão com o WebService do TOTVS MES. Favor verificar as configurações de conexão. Erro:****Resposta:** Estas mensagens podem ocorrer quando o serviço de **webservice** não está no ar.
3. **O link é um wsdl válido. Porém não contém os métodos utilizados para integração com o TOTVS MES. Favor verificar as configurações de conexão.****Resposta:** Não foi possível identificar na mensagem qual é a operação que deverá ser realizada inclusão/alteração/modificação/exclusão.
4. **Não conseguiu setar a operação XXXX. Erro: XXX****Resposta:** Não foi encontrada a *tag* **Event** no **XML** gerado/enviado.
5. **Não foi possível utilizar o XML. Erro:****Resposta:** O **XML** informado está com o formato inválido ou com algum erro nas suas *tag´s.* Deverá ser verificado se o **xml** está em um formato válido e com as *tag´s* do **XML** sendo abertas e fechadas corretamente.
6. **Não foi possível realizar o parse do XML de retorno do TOTVS MES.****Resposta:** O endereço da *tag* **TOTVSMessage** está inválido.
7. **O diretório '" XXX "' é inválido.****Resposta:** Os diretórios informados nos campos: **Enviados** e **Pendência** do **PCPA109** estão incorretos ou não existem.  
   Campos do **PCPA109** que devem ser revisados:  
   - Gera **XML** - Ao selecionar esse campo, irá gerar os **XML** das mensagens trocadas. Se não estiver selecionado, será gravado apenas em tabelas. A geração dos arquivos não é obrigatória. Serve como uma ferramenta útil para encontrar problemas. O envio sempre será feito com base do que estiver registrado nas tabelas;  
   - **Enviados** - Diretório onde serão salvos os **XMLs** enviados com sucesso ao **PC-Factory**;  
   - **Pendência** - Diretório onde serão salvos os **XMLs** que não foram enviados ao **PC-Factory**.
8. **Erro ao criar o arquivo XML no diretório '" XXX "'. Erro:****Resposta:** Verificar se o usuário possui permissão de gravação nos diretórios informados no **PCPA109** ou se o nome do diretório possui algum caracter especial.
9. **Não é possível enviar XML com caracteres especiais. Por favor, revise o cadastro do Produto XXXX****Resposta:** O cadastro de operações no **MATA632/PCPA124** possui caracteres especiais e devem ser retirados.  
     
   Abaixo, há alguns exemplos de caracteres que podem causar problemas no envio da mensagem de **Operações** para o **Totvs MES** e a recomendação é retirá-los do cadastro:
   * €
   * ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069254134/mceclip0.png)
   * Ž
   * ü
   * ì
   * Å
   * É
   * ¥
   * (
   * )

**Importante**P**ara o MATA632** essas mensagens estão disponíveis a partir da **versão 11.80**.  
Já para o **PCPA124** essa mensagens estão disponíveis a partir da **versão 12.1.30.**  
  
**Saiba mais****Referente ao item 2**:  segue documentações complementares:[URLs acessadas pela TWsdlManager](https://tdninterno.totvs.com/display/tec/URLs+acessadas+pela+TWsdlManager) e [TWsdlManager:ParseURL](https://tdninterno.totvs.com/display/tec/TWsdlManager%3AParseURL) **Referente ao item 9**: Para maiores informações sobre os caracteres acesse a documentação: [EncodeUTF8](https://tdn.totvs.com/display/tec/EncodeUTF8)Informações mais detalhadas sobre a integração **TOTVS MES**, podem ser encontradas no **Manual**: [Integração PCP Protheus x PPI-Multitask](https://tdn.totvs.com.br/pages/releaseview.action?pageId=208340274)
