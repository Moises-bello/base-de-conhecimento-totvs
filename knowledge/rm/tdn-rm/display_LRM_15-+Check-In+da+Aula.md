---
content_hash: 392d41d08f1307f9c34114d62fb00ba36042c6d153c72f8f2078e00adc9b2e52
fetched_at: '2026-06-29T00:12:14.209098+00:00'
page_id: '967096555'
product: rm
source: tdn-rm
title: 15- Check-In da Aula
type: documentation
url: https://tdn.totvs.com/display/LRM/15-+Check-In+da+Aula
version: 3
---

false

Essa funcionalidade está disponível a partir da versão:

* Totvs Gestão Educacional: 12.1.2209.100
* App Meu eduCONNECT: 08.2209.03

O check-in da aula,  tem como objetivo o aluno realizar um check-in na aula, através do App por Localização, colocando como premissa o endereço (aproximado) onde o Aluno está localizado.

O check-in realizado será validado posteriormente, baseado em diversos critérios definidos pela instituição, e a falta (do check-in) poderá ser registrada automaticamente no processador da frequência diária.

O aluno não precisará se preocupar em selecionar aulas, pois o sistema identificará automaticamente pelo dia e horário da aula em que o aluno está matriculado, e que deveria registrar ao menos um check-in.

Parametrização

Primeiramente, é necessário que a Instituição de Ensino configure:

**1º)** O [URL Rewrite](https://tdn.totvs.com/x/RURGIQ) e o [Application Request Routing Cache (ARR)](https://tdn.totvs.com/x/2vzAI) ;

**2º)** Configurar a URL do FrameHTML ([http://Nome\_do\_Servidor/FrameHTML](http://10.173.11.197/FrameHTML)) em: **Ambiente | Parâmetros | Parâmetros Globais |Frame HTML**

Entendendo a funcionalidade

O check-in da aula possui duas modalidades para a realização do check-in que estão basicamente ligadas ao nível de segurança, sendo:

* Check-in por Localização (liberado na release 12.12209.100);

### Premissas para usar corretamente a funcionalidade de check-in no app Meu eduCONNECT:

* O aluno tenha uma matrícula no período letivo e que o mesmo esteja ativo;
* O check *"Exibir no Portal do aluno"* no cadastro do período letivo deverá estar marcado.
* Na situação de Matrícula no Período Letivo o parâmetro: "*Visível para seleção no contexto educacional do Portal"* (Aba: "Portal"), deverá estar marcado;

Caso apareça a mensagem: *Aluno não possui contextos válidos*, ao acessar o menu check-in da Aula no App Meu eduCONNECT, validar as opções de acesso a funcionalidade .

Check-in por Localização

O Check-in por localização **é realizado apenas pelo App Meu eduCONNECT**, onde o Aluno irá realizar o check-in de acordo com a localização (latitude e longitude).

Essa funcionalidade está parametrizada como default no sistema (entrar em contato com o suporte para habilitar essa funcionalidade), isso é, a partir do momento que a funcionalidade for liberada, a Instituição de Ensino terá acesso à funcionalidade, mediante a parametrização.

# **Meu eduCONNECT**

### Menu: CHECK-IN DA AULA

Para acessar a funcionalidade, o Aluno deverá ter a permissão em: **Serviços Globais | Segurança | Perfil | "Sistema" Educacional | eduCONNECT | Check-In da Aula.**

Permissão necessária

É necessário que ao logar no App, o Aluno dê permissão de acesso a **Localização.**

**Localização**: (Obrigatório) Para que seja capturado o endereço (latitude e longitude) para identificar a localização do registro do check-in.

Ao logar no App: Meu eduCONNET  e clicar no menu: Check-In da Aula, será exibido a mapa com a data e horário e a localização atual do aluno, conforme o print abaixo.

 Para registrar a frequência, o aluno deverá pressionar o botão: "**Pressione para registrar**" e aguardar alguns milésimos de segundos ( o botão será preenchido enquanto a presença está sendo registrada).

Após registrar a frequência, o App irá apresentar uma mensagem de feedback, informando que a frequência foi registrada e a presença será liberada posteriormente.

false

O aluno irá apenas registrar o check-in e a validação e liberação da mesma fica a cargo da instituição de ensino através do processo **[Processador da frequência diária](https://tdn.totvs.com/x/r753Kg)**.

Processador da Frequência Diária

Após o aluno realizar o check-in, a instituição de ensino deverá processar a frequência de acordo com os registros inseridos no check-in do aluno por Localização o através do: [Processador da frequência diária](https://tdn.totvs.com/x/r753Kg).

Banco de Dados

## **Tabela envolvida**

SCHECKINAULA
