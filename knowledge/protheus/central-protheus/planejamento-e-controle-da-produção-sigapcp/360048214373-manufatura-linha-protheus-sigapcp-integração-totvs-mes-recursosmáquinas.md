---
article_id: 360048214373
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a7e368f1e206448975e3bdf506dca37ea0e7e4824ce522d2dd03eae919edeb5a
fetched_at: '2026-06-28T22:42:43.487490+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Integração TOTVS MES - Recursos/Máquinas
type: support-article
updated_at: '2024-04-29T17:53:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048214373-Manufatura-Linha-Protheus-SIGAPCP-Integra%C3%A7%C3%A3o-TOTVS-MES-Recursos-M%C3%A1quinas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:05:30 min**  
**Ocorrência**  
Ao efetuar a integração do cadastro de **Recursos/Máquinas –** **MATA610, SFCA006 e SFCA002** via **TOTVS MES**, apresenta mensagens de inconsistência.  
   
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Essas mensagens podem ocorrer, por configuração incorreta do **WebService** ou no **Cadastro de Recursos/Máquina**.  
  
 **Solução**  
No momento da criação, alteração ou exclusão de um recurso nos programas **MATA610** ou **SFCA006** ou **SFCA002** e **MATA620** - **Ferramentas**, é verificado se a integração está ativa para enviar o cadastro para o **PC-Factory**. Caso não ocorrer erro, o cadastro não apresentará nenhuma mensagem, porém se ocorrer erro uma mensagem será exibida questionando se deseja criar uma pendência de envio no programa **PCPA110**. Se optar por gerar a pendência o processo, será efetivado no **Protheus** e a atualização para o **PC-Factory** deverá ser realizada por meio do **PCPA110**.  
  
As seguintes mensagem de inconsistência podem ser apresentadas:

1. **Não existe caminho de WebService cadastrado. Verifique os parâmetros da integração.****Resposta:** Deve-se informar um **webservice** válido no **PCPA109** no campo **caminho**.   
   **Caminho**: Indica o caminho do **WebService** do **PC-Factory**. Após o caminho, terá um botão **testar** para verificar se **webservice** está ativo.
2. **Não foi possível realizar a conexão com o WebService do TOTVS MES. Favor verificar as configurações de conexão. Erro:****Resposta:** Estas mensagens podem ocorrer quando o serviço de **webservice** não está no ar.
3. **O link é um wsdl válido. Porém não contém os métodos utilizados para integração com o TOTVS MES. Favor verificar as configurações de conexão.****Resposta:** Não foi possível identificar na mensagem qual é a operação que deverá ser realizada inclusão/alteração/modificação/exclusão.
4. **Não conseguiu setar a operação XXXX. Erro: XXX****Resposta:** Não foi encontrada a *tag* **Event**”no **XML** gerado/enviado.
5. **Não foi possível utilizar o XML. Erro:****Resposta:** O **XML** informado está com o formato inválido ou com algum erro nas suas *tag´s*. Deverá ser verificado se o **xml** está em um formato válido e com as *tag´s* do **XML** sendo abertas e fechadas corretamente.
6. **Não foi possível realizar o parse do XML de retorno do TOTVS MES.****Resposta:** O endereço da *tag* **TOTVSMessage** está inválido.
7. **O diretório '" XXX "' é inválido.****Resposta:** Os diretórios informados nos campos: **Enviados** e **Pendência** do **PCPA109** estão incorretos ou não existem.  
     
   Campos do **PCPA109** que devem ser revisados:  
   - **Gera XML** - Ao selecionar esse campo, irá gerar os **XML** das mensagens trocadas. Se não estiver selecionado, será gravado apenas em tabelas. A geração dos arquivos não é obrigatória. Serve como uma ferramenta útil para encontrar problemas. O envio sempre será feito com base do que estiver registrado nas tabelas;  
   - **Enviados** - Diretório onde serão salvos os **XMLs** enviados com sucesso ao **PC-Factory**- **Pendência** - Diretório onde serão salvos os **XMLs** que não foram enviados ao **PC-Factory.**
8. **Erro ao criar o arquivo XML no diretório '" XXX "'. Erro:****Resposta:** Verificar se o usuário possui permissão de gravação nos diretórios informados no **PCPA109** ou se o nome do diretório possui algum caracter especial.
9. **Não é possível enviar Xml com caracteres especiais. Por favor, revise o cadastro de Recursos XXXX****Resposta:** O cadastro de **Recursos** no **MATA610/SFCA002/SFCA006** possui caracteres especiais e devem ser retirados.  
     
   Abaixo, há alguns exemplos de caracteres que podem causar problemas no envio da mensagem de **Recursos/Máquina** para o **Totvs MES** e a recomendação é retirá-los do cadastro:
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

Quando o cliente utiliza somente o **PCP - Planejamento e Controle da Produção**, as máquinas são cadastradas na rotina de recursos **MATA610** e quando o cliente utiliza o **Chão de Fábrica**, a rotina de cadastro é o **SFCA002**. A nomenclatura também é alterada. Quando utilizar o **Chão de Fábrica**, será denominada **Máquina** e quando utilizar somente o **PCP**, será **Recurso**. A rotina **PCPA109 - Parâmetros** está preparada para apresentar o nome de acordo com o uso do Sistema.  
  
Tanto no **PCPA110 - Pendências**, quando no **PCPA109** haverá as opções:

* **Recurso PCP**
* **Recursos do chão de fábrica - Ferramentas, Equipe e Operador**

**Importante**

* O **Recurso** no **PCP** indica a máquina, no **Chão de Fábrica** indica ferramentas, operador, etc.;
* Quando origem for do **PCP** a *tag* **Type** **- Tipo Recurso** será gerada com o valor fixo **2**;
* Quando origem for do **PCP** a *tag* **UnitCycleQuantity - Unidades Ciclos** será gerada com o valor fixo **1**;
* Quando origem for do **PCP** a *tag* **UnitCycleQuantity - Unidades Ciclos** será gerada com o valor fixo **1**;
* Quando origem for do **PCP** a *tag* **StartExpirationDate - Validade Inicial** será gerada com a data de geração da mensagem;
* Quando origem for do **PCP** a *tag* **EndExpirationDate - Validade Final** será gerada com o seguinte cálculo:  **dDataBase + H4\_VIDAUTI**, onde **dDataBase - Data atual  e** **H4\_VIDAUTI - Vida útil da ferramenta**.  
  Considerar o tipo de **Vida útil - H4\_TIPOVID:**  **D - Dias**; **H - Horas**; **M - Mês**; **A - Ano**.

**Saiba mais**  
1) **Referente ao item 2**: Também pode ser verificado o link [URLs acessadas pela TWsdlManager](https://tdninterno.totvs.com/display/tec/URLs+acessadas+pela+TWsdlManager) e [TWsdlManager:ParseURL](https://tdninterno.totvs.com/display/tec/TWsdlManager%3AParseURL)

2) **Referente ao Item 9:** Maiores informações: [EncodeUTF8](https://tdn.totvs.com/display/tec/EncodeUTF8)3) **Cadastro de Máquina:** O ponto de entrada **MTI610UTTP** permite alterar o valor enviado na *tag* **UnitTimeType**. Detalhes em: [MTI610UTTP - Alterar o valor da tag UnitTimeType da mensagem Machine](http://tdn.totvs.com/display/PROT/MTI610UTTP+-+Alterar+o+valor+da+tag+UnitTimeType+da+mensagem+Machine).  
  
4) Informações mais detalhadas sobre a integração **TOTVS MES**, podem ser encontradas no **Manual**: [Integração PCP Protheus x PPI-Multitask](https://tdn.totvs.com.br/pages/releaseview.action?pageId=208340274)
