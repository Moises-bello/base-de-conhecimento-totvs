---
content_hash: 75ab691e3e7ba48940a69283d0cc25d463a2338b3e21b0ecfa30944a87bd1549
fetched_at: '2026-06-29T00:09:49.288427+00:00'
page_id: '435105274'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Configuração e Parametrização.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105274
version: 22
---

Para a utilização do PDC, é necessário executar algumas configurações e parametrizações na base.

Configuração e Parametrização do PDCConfigurandoConfiguração para versão acima de 12.1.2502

Obrigatório subir o HOST como Administrador - Configuração necessária para versão 12.1.2502 em diante.

Verificar o arquivo : config.json se a porta é a mesma da TAG APIPort do Host como a imagem abaixo.

**Caminho que fica o arquivo config.jason :** web\app\imb\PortalCliente\config

CONFIG DO HOST:

CONFIG.JSON: Colocar no arquivo config.json a url da api, já com o endereço para acesso externo, caso seja um ambiente que será acessado via web.   
Caso tenha dúvidas sobre como expor a API e o Webservice, . Após expor é necessário que seja criado uma regra de  
redirecionamento do DNS e Porta que a api estará disponível, para  o servidor onde o host esta iniciado, na mesma porta.

E ao subir o Host, subir como **Administrador.**

**Primeiro é necessário informar nos *Parâmetros Globais -> Gerais*, no campo "URL de acesso ao Portal RM", a Url base do Portal Corpore .Net. Exemplo:**

Testando a instalação e configuração do Portal do Cliente.

Para garantir que a instalação e configuração das tags foram bem sucedidas, recomenda-se reiniciar o **RM.Host** e realizar os seguintes testes:

### 🔧 **Verificando o Ambiente de APIs – Portal do Cliente**

Para garantir que o Portal do Cliente está corretamente integrado com o ambiente de APIs da TOTVS, siga os passos abaixo:

---

#### ✅ **Passo 1: Acesse o Navegador**

Abra seu navegador de internet (como Google Chrome, Microsoft Edge ou Firefox).

---

#### ✅ **Passo 2: Digite o Endereço da Interface Swagger**

No campo de URL do navegador, digite o seguinte endereço:

`http://{url do ambiente}/api/swagger/ui/index`

> **Atenção:**  
> Substitua `{url do ambiente}` pelo endereço do servidor onde o ambiente TOTVS está configurado.  
> Exemplo: `http://{url do ambiente}/api/swagger/ui/index`

---

#### ✅ **Passo 3: Verifique a Tela de Retorno**

Se o ambiente estiver configurado corretamente, você verá uma tela semelhante à imagem abaixo, indicando que o serviço de APIs está ativo e operando normalmente:

📸

**Observação:**  
No exemplo apresentado, o endereço exibido é `localhost` porque o servidor está configurado localmente em meu computador.  
Além disso, a porta utilizada é a **8051**, conforme definido nos arquivos de configuração `Config.json` e `Host.config`.

---

#### ❗ **Em caso de erro**

Se a tela não for exibida ou aparecer alguma mensagem de erro (como "Página não encontrada" ou "Erro de conexão"), verifique:

* Se o servidor está ligado.
* Se a URL foi digitada corretamente.
* Se as portas necessárias estão liberadas no firewall.

**Segundo passo é informar nos *Parâmetros Globais -> Frame HTML*, no campo "Defina o endereço do Frame HTML:", a URL Base do Totvs Frame HTML hospedado.. Exemplo:**

Conifgurando no RM e IIS para usar o PDC.

Neste exemplo é : localhost:8070     
  
Configurando porta no IIS.

### 🔐 **Testando a Autenticação via API**

Utilize uma ferramenta de testes de API, como o **Postman**, para realizar uma requisição do tipo **POST** para o seguinte endereço:

**http://{url do ambiente}/api/connect/token**

Se a autenticação estiver configurada corretamente, a resposta será semelhante à mostrada no exemplo abaixo, indicando que o serviço de geração de token está funcionando normalmente.

1º = Tipo POST

2º = Em Body - Marcar opção ( x-www-form-urlencoded )

3º = Neste exemplo acima foi inserido **username** utilizado o usuário "mestre" e  **password** com a senha "totvs".

4º = {  
    "access\_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg4QjE0REZCQUNBMDZBMjk4OEQ5MUI3NDMxNkVBNTRCQ0Y3NzlEMzYiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJtZXN0cmUiLCJodHRwOi8vd3d3LnRvdHZzLmNvbS9ybS9jb25uZWN0aW9uSWQiOiJDb3Jwb3JlUk0iLCJ0ZW5hbnRJZCI6IjkzMDk3ZDM1LWY0MjktNDQwMS1iNTE4LTM0OTcwYjAwYzgzZiIsIm5iZiI6MTc0NDkxMzI3MSwiZXhwIjoxNzQ0OTE1MDcxLCJpYXQiOjE3NDQ5MTMyNzEsImlzcyI6InRvdHZzLXJtLWhvc3QifQ.hVJcR3RRNHBau0vZ4gE46dIBEz4sU0mgxrkIzg7ZJtokMVcn61OLh0xCq\_BmtvEIVqZDJQ3Ikrn51jx8lK66Ps8AShxqcI38VoErhOXgRanuSgH\_P5xyt851yacEGedrmc3RDr2xEKr\_7mHEbW6Yp7qW3rbCua0WwlutaoHEmI6hqGVAqjVoRNgRuaCqDp6tRRXjUwJLvVQYA4MyImvZlVAgpAlQU33sWhfpddp0feTFR56cOBfZ\_PMcZHpBHcl-WTPsypzvUgx1rzfqmn4nOY68RuawLVWa\_BVrf5IyemvmGzEUAdqE1Bo3lPYNOxgnAQIu-pqpjTcitVJYc5fggQ",  
    "expires\_in": 1800,  
    "refresh\_token": "eyJUb2tlbktleSI6InNXSTRCUmtFYUdzTGpoQWxGcnNXSFZMR1dKWDE1cHA4OWJZZDlQeG5zIiwiY29ubmVjdGlvbklkIjoiQ29ycG9yZVJNIn0=",  
    "token\_type": "Bearer"  
      }

Mostrando que o teste foi executado com sucesso.

### 📝 **Observações Importantes**

Para a realização deste teste, atente-se aos pontos destacados na imagem acima.

Na aba **"Headers"** da ferramenta de testes (como o Postman), é necessário informar os seguintes parâmetros:

**Key :** Content-Type

**Value :** application/x-www-form-urlencoded

ParametrizandoTotvs-app-global-config.js

Importante configurar o arquivo ( Totvs-app-global-config.js ) que fica localizado dentro da pasta FrameHtml\Web\Js com caminho do PDC instadado.

Neste exemplo o cliente deve colocar FrameHTML ao entrar no portal do cliente.

Para as funcionalidades do Portal do Cliente, existe os seguintes parâmetros para o Totvs Incorporação e para o Totvs Gestão Financeira:

* Parâmetros do Financeiro estarão disponíveis no caminho *Contas a Receber>>Integração Bancária*:

* + **Convênio padrão para Registro Online:** A geração de um novo boleto com registro online precisa de um convênio bancário padrão que deverá ser estabelecido nos parâmetros financeiros. O usuário só poderá escolher entre convênios que tenham a opção de Registro online marcado. Não permitir desmarcar a configuração de registro online do convenio que esteja sendo utilizado na parametrização; Não permitir desativar o convenio ou a conta financeira configurada no registro online do convenio que esteja sendo utilizado na parametrização;

* Parâmetros do Incorporação estão disponíveis nos seguintes caminhos:

*Imobiliária >> Portal do Cliente >> Relatórios*

* + **Boletos:**
    - **Permite Gerar Novo Boleto para Parcelas Vencidas:** nem todas as empresas permitem que sejam gerados novos títulos para parcelas já vencidas sendo necessário a parametrização para que cada cliente estabeleça seus próprios critérios
    - **Permite Antecipação de Pagamento:**  Parâmetro no TIN, onde a incorporadora indica se o portal TIN deve ou não disponibilizar parcelas financeiras com vencimento futuro para antecipação do pagamento. Para o correto funcionamento do recurso de Antecipação de Pagamento, o recurso de reajuste online do financeiro deve estar ativado para cálculo de valores contratuais(Juros e CM) , caso contrário não haverá atualização dos valores contratuais.
    - **Opções de pagamento para as parcelas:**É possível que o usuário efetue o pagamento da parcela via PIX através do parâmetro "PIX: Integrado com o TDP".
    - **Tipo de Geração de Boletos :** Este parâmetro define se novos boletos ou a antecipação de boleto será feita pelo processo de registro online ou pelo processo de gerar boletos não registrados.
    - **Relatório para impressão de boletos não registrados:** Neste parâmetro deve ser selecionado o relatório do RM Report's, que será a base para a geração de boletos. É importante lembrar que este relatório precisa ter como parâmetros os campos: COLIGADA, IDLAN, DATAEMISSAO, DATAVENCIMENTO, VALORPARCELA, NOSSONUMERO, IPTE, CODIGOBARRAS.

Para mais informações sobre o processo de Geração de Boletos no Portal do Cliente, .

* **Relatórios:**
  + **Relatório para impressão da Ficha Financeira:** Define qual modelo de relatório será impresso na opção de Ficha Financeira no Portal do Cliente.
  + **Relatório para impressão do Informe de Pagamento - IR:** Define qual modelo de relatório será impresso na opção de Informe de Pagamento no Portal do Cliente.

Para mais informações sobre os Relatórios do Portal do Cliente, .

*Imobiliária >> Portal do Cliente >> Renegociação de Contrato*

* + - **Permite efetivação automática da renegociação de contrato:** Informa se a renegociação elaborada pelo comprador será efetivada de forma automática pelo sistema ou se o novo plano será efetivado pelo setor responsável. Caso este parâmetro esteja marcado, a aprovação automática estará condicionada aos dois próximos parâmetros abaixo, que estarão habilitados para edição:
      * **Valor máximo para renegociação:** Valor máximo permitido a ser renegociado, ou seja, a soma das parcelas vencidas.
      * **Número máximo de parcelas:** Quantidade máxima de parcelas permitidas para o novo plano.
    - **Número de dias corridos para o primeiro vencimento:** Informa a quantidade de dias corridos que o sistema utilizará para calcular o vencimento da primeira parcela do novo plano. Portanto a data do primeiro vencimento será igual a data que o aditivo foi criado mais o número de dias definido nos parâmetros.
    - **E-mail do(s) responsáveis pela aprovação:** Informa quais e-mails devem ser comunicados quando o comprador executa determinadas ações no Portal. Os seguintes cenários geram e-mail:
      * Comprador gera uma nova renegociação e a mesma foi efetivada de forma automática.
      * Comprador gera uma nova renegociação e a mesma aguarda análise e aprovação.
      * Comprador cancelou uma renegociação que estava na situação em preparação.

Para mais informações sobre a Renegociação de Contrato do Portal do Cliente, .

Veja Também
