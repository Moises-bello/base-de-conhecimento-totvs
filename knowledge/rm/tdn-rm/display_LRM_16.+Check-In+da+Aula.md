---
content_hash: 9e3bf524670f4ccc30ed2c2c728d4e0ae103b78e18700d6a4baf0a1be936fe93
fetched_at: '2026-06-29T00:12:14.216123+00:00'
page_id: '967096639'
product: rm
source: tdn-rm
title: 16. Check-In da Aula
type: documentation
url: https://tdn.totvs.com/display/LRM/16.+Check-In+da+Aula
version: 8
---

O check-in de aula tem como objetivo registrar a presença do aluno por meio do aplicativo, utilizando sua localização aproximada como referência.

Após o envio, o check-in poderá ser validado posteriormente pela instituição, com base em critérios previamente definidos. Caso não seja realizado, a ausência poderá ser registrada automaticamente no processador de frequência diária.

O aluno não precisa escolher manualmente a aula: o sistema identifica automaticamente, pelo dia e horário, a aula em que ele está matriculado e para a qual deve registrar o check-in.

Configuração inicial necessária pela Instituição de Ensino

Antes de utilizar a funcionalidade, a instituição de ensino deve realizar as seguintes configurações:

1. O [URL Rewrite](https://tdn.totvs.com/x/RURGIQ) e o [Application Request Routing Cache (ARR)](https://tdn.totvs.com/x/2vzAI) ;
2. Configurar a URL do FrameHTML ([http://Nome\_do\_Servidor/FrameHTML](http://10.173.11.197/FrameHTML)) em: **Ambiente | Parâmetros | Parâmetros Globais |Frame HTML**

Permissão de acesso

Para acessar a funcionalidade, o aluno deverá ter a permissão em: **Serviços Globais | Segurança | Perfil | "Sistema" Educacional | eduCONNECT | Check-In da Aula**

Alunos disponíveis

O check-in será exibido ao aluno no app apenas quando forem atendidas as seguintes condições:

1. O aluno possui matrícula ativa no período letivo vigente;
2. No cadastro do período letivo, a opção **“Exibir no Portal do Aluno”** está habilitada;
3. Na matrícula do aluno no período letivo, o parâmetro **“Visível para seleção no contexto educacional do Portal”** (aba *Portal*) está marcado.

Caso seja exibida a mensagem “Aluno não possui contextos válidos” ao acessar o menu de Check-in da Aula no app Meu eduCONNECT, é necessário validar se as regras de exibição da funcionalidade.

Check-in por Localização

O check-in por localização é realizado exclusivamente pelo aplicativo Meu eduCONNECT, utilizando as coordenadas de latitude e longitude para registrar a presença do aluno.

Essa funcionalidade encontra-se disponível no sistema, porém sua ativação depende de parametrização. Para habilitá-la, é necessário entrar em contato com o suporte. Após a liberação, a Instituição de Ensino poderá configurar os parâmetros necessários e disponibilizar o recurso aos alunos.

Permissão de Localização

Para utilizar o check-in por localização, é necessário que, ao acessar o App Meu eduCONNECT, o aluno conceda permissão de uso da localização do dispositivo.

A permissão de **Localização (obrigatória)** é utilizada para capturar as coordenadas (latitude e longitude) e identificar o local onde o check-in foi realizado.

false

O aluno apenas realiza o registro do check-in; a validação e a liberação da presença ficam a cargo da instituição de ensino, por meio do **Processador da Frequência Diária**.

Ao acessar o app **Meu eduCONNECT** e selecionar o menu **“Check-in da Aula”**, será exibido um mapa com a **data e horário da aula**, além da **localização atual do aluno**, conforme demonstrado na imagem abaixo.

Para registrar a frequência, o aluno deverá pressionar o botão **“Pressione para registrar”** e aguardar alguns instantes. Enquanto o check-in estiver sendo processado, o botão será preenchido visualmente até a confirmação do registro.

Após o registro da frequência, o aplicativo apresentará uma mensagem de confirmação informando que o check-in foi realizado com sucesso e que a presença será validada e liberada posteriormente pela instituição.

IMPORTANTE - Dispositivos iOS 14 ou superior

**Permissões necessárias no iOS (App Tracking Transparency e Localização)**

A partir da versão **08.2506.07**, para que o aluno consiga realizar o check-in da aula no app Meu eduCONNECT, é necessário conceder permissão ao recurso **App Tracking Transparency**, disponível em dispositivos **iOS 14 ou superior**.

Após o login, o aplicativo exibirá a solicitação dessa permissão. O usuário deverá selecionar **“Permitir” (Allow)** para prosseguir e garantir o funcionamento do recurso.

> **Observação:** Além da permissão de App Tracking Transparency, também é obrigatório conceder a permissão de **acesso à localização** do dispositivo, pois é ela que permite capturar as coordenadas (latitude e longitude) utilizadas no registro do check-in.

Caso o usuário marque a opção **"Peça ao aplicativo para não rastrear" (Ask App not to Track),**  ao abrir a tela de check-in da aula, será apresentado a mensagem abaixo solicitando a parametrização dessa configuração.  

Caso o dispositivo não esteja exibindo a configuração de "Permitir Rastreamento", será necessário realizar o passo a passo abaixo:

* Abra o app **Ajustes**.
* Toque em **Privacidade e Segurança**.
* Toque em **Rastreamento**.
* Ative a chave **Permitir que apps solicitem rastreamento**

Processador da Frequência Diária

Após o aluno realizar o check-in, a instituição de ensino deverá processar a frequência com base nos registros de localização do aluno, utilizando o **[Processador da frequência diária](https://tdn.totvs.com/x/r753Kg)**.

Tabelas do banco de dados relacionada

## 

SCHECKINAULA
