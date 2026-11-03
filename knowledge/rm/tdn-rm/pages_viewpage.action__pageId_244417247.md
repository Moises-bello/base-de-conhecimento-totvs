---
content_hash: 8c54aed80b29b4d2238474269053e7411c74f46228ef92f5f1a9a690336d6e4f
fetched_at: '2026-06-29T00:08:13.370207+00:00'
page_id: '244417247'
product: rm
source: tdn-rm
title: Criação de Servidor de Aplicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244417247
version: 14
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Com o servidor de aplicação podemos limitar o número de registros mostrados na visão.

O sistema por default permite que sejam apresentados apenas 500 registros nas visões de modo a melhorar o desempenho do sistema.

## **02. EXEMPLO DE UTILIZAÇÃO**

**VERSÃO 12.XX**

**NOVA MDI**

**acesse:**Serviços globais | Serviços | Servidores de aplicação

Deve-se criar um novo Servidor de Aplicação com o número máximo de registros, por exemplo, 5000.

Para tanto, inicialmente faz-se necessário ter conhecimento do nome da Action que será realizada a liberação dos registros.

Essa informação pode ser solicitada à equipe do aplicativo, neste caso, o cliente deverá entrar em contato com o suporte do RM Saldus, e solicitar o nome da Action.

Ou, poderá acessar a visão novamente, se atentando para o nome da Action que é apresentada ao se carregar a visão. O nome da Action estará visível no canto inferior da tela, à esquerda:

**OBSERVAÇÃO:** Nem sempre o nome é o mesmo, portanto, é necessário confirmar o mesmo com o aplicativo.

Tendo conhecimento do nome da Action, crie o Servidor de Aplicação com o número de registros desejado:

Neste caso, o nome da Action utilizada será CtblanData.

 

 

Após criação do Servidor de Aplicação, ao **acessar** a visão de Lançamentos -> Manutenção de Lançamentos, todos os registros serão apresentados, até o novo limite configurado:

### **EXEMPLO DE CRIAÇÃO DE SERVIDOR DE APLICAÇÃO VIA MDI**

Para localizar Actions via MDI utilize o menu executar no canto a direita, informe o nome da Action e posicione o mouse sobre a mesma.

Outra forma de identificar o nome da Action, é selecionar o atalho Ctrl+Alt+F9 na tela, será apresentada uma janela com o nome da Action:

Informe o número máximo de registros, por exemplo, 5000:

Os campos Registro Automático e Notifica Registro não são editáveis, ou seja, são disponíveis apenas para consulta. Cabe aos produtos determinarem se é necessário usá-los.

Ao usar o registro automático, o serviço fica registrado ao subir o Host. Assim, ele será registrado e o serviço ficará na memória.  
Ao usar o notifica registro, no momento que o serviço é chamado, ele é registrado no host e os outros hosts também devem subir este serviço.

Os campos aparecerão marcados quando:

• Registro automático: a classe implementar a IRMSServerAutoRegister  
• Notifica registro: a classe implementar a IRMSServerNotifyRegister

### **EXEMPLO DE CRIAÇÃO DE SERVIDOR DE APLICAÇÃO PARA ACTION DE METADADOS**
