---
content_hash: 59d1bb0af1da0f81249dce8811b6967869d2806404b696babc9b2c6c788a4386
fetched_at: '2026-06-29T00:11:17.361959+00:00'
page_id: '679167421'
product: rm
source: tdn-rm
title: Painel de chamadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Painel+de+chamadas
version: 21
---

PainelVisão GeralAtenção

A partir da versão 12.1.2302.157, os webservices que utilizam TBC **(TOTVS Business Connect)** via IIS passam a utilizar TBC via Host, confirme orientação enviada em Comunicado de descontinuação: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/9198729724439-Aviso-de-substitui%C3%A7%C3%A3o-Integra%C3%A7%C3%A3o-TBC-via-IIS-para-TBC-via-Host-Linha-RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9198729724439-Aviso-de-substitui%C3%A7%C3%A3o-Integra%C3%A7%C3%A3o-TBC-via-IIS-para-TBC-via-Host-Linha-RM "Follow link")

Link contendo orientações [Como Expor os Web Services do RM através do Host (recomendado)](https://tdn.totvs.com/pages/viewpage.action?pageId=89620766) :  <https://tdn.totvs.com/x/HoFXBQ>

Link para Listagem dos Webservices do TBC - **Totvs Gestão Hospitalar (wsSau)** :  <https://tdn.totvs.com/x/ev9bGQ>

1 - Em Caso de Ambiente Cloud, é necessários acrescentar as seguintes tags no arquivo Web.config do Painel de Chamadas:

<!-- Tags necessárias para ambiente Cloud (HTTPS) -->

    <add key="ServicesHostName" value="[url.rm.cloudtotvs.com.br](http://suzanclin109771.rm.cloudtotvs.com.br)"/>  
    <add key="WS-Server" value="https://url.rm.cloudtotvs.com.br:8051"/>  
    <add key="TLS" value="True"/>

2 - Os arquivos necessários para utilização do Painel encontram-se no Drive da Tribe Saude, link  <https://drive.google.com/drive/folders/1f1g952TrQ1CTmUcHhAX6rLYSS3Pi5JFk?usp=drive_link>

Novidade na Versão 12.1.2506

A partir da versão **12.1.2506**, o sistema permite a customização para exibir o **local de origem** no histórico de senhas chamadas.

Para habilitar essa funcionalidade, consulte as instruções no menu de **Informações Técnicas** deste manual.

Chamada de voz com API Text-to-Speech (opcional)

**Chamada de voz com API Text-to-Speech (opcional)**

Funcionalidade disponível a partir da versão 12.1.33  
Especialmente para Smart TV (LG/Sansung)

Controle de documento1. Criação de token

1. **Criação de token**

O processo de criação do token para acesso à API do Google Text to Speech começa ao acessar este [link](https://console.cloud.google.com/apis/). (opcional)

Ao acessar clique em Criar Projeto

Escolha o nome do Projeto e o Local como mostra a figura abaixo e clique em criar

Ao criar vai abrir o projeto, então selecione no menu a esquerda a opção Credenciais, ao clicar vai aparecer a tela abaixo

Então clique em Criar Credenciais e escolha a opção Chave de API

A chave será gerada

Após clique no menu de navegação e vá em APIs e serviços e selecione Biblioteca

Em Biblioteca encontre Text to speech API e ative.

Agora é necessário vincular uma conta de faturamento, no menu de navegação clique em Faturamento, ao abrir a tela clique em Vincular Conta de Faturamento, caso não tenha uma conta de faturamento clique em criar conta de faturamento.

Siga os passos e ao final faça o cadastro dos dados solicitados

Ao finalizar o cadastro vai aparecer a seguinte informação, que fala que você tem 1 mês de teste gratuito, você só é cobrado caso passe do limite estipulado por tipo de voz.  
O consumo foi construído com o tipo de voz mais baixo.

Para mais informações sobre veja [Tabela de preços](https://cloud.google.com/text-to-speech/pricing)

2. Configuração no parâmetros gerais

2. **Configuração no parâmetros gerais**

**Opções > Parâmetros > Parâmetros Gerais > Aba Integrações > Aba Google API**

Insira o token criado no passo 1 em "Chave Google API Text To Speech"

Acesse o painel normalmente e use.

Com o token ativado e configurado no parâmetros gerais ao acessar o painel pode se validado o correto funcionamento conforme abaixo

Informações TécnicasInformações Técnicas

**Informações técnicas para customização:**

**Layout**

Ao customizar o frontend do painel, observe a estrutura do array de dados. Esse array, utilizado nos arquivos **main.js** e **painel.aspx**, é fundamental para a correta montagem do layout.

As informações são ordenadas de uma maneira específica, e é crucial que essa ordem seja mantida para garantir a funcionalidade e o bom funcionamento do painel.

labelValues[0] = Senha  
labelValues[1] = Nome;  
labelValues[2] = Local;  
labelValues[3] = TipoFila;  
labelValues[4] = Especialidade;  
labelValues[5] = ImgPreferencial ("T" ou "F");  
labelValues[6] = DescUnidade;  
labelValues[7] = Triagem01.Senha;  
labelValues[8] = Triagem01.Local;  
labelValues[9] = Triagem02.Senha;  
labelValues[10] = Triagem02.Local;  
labelValues[11] = Triagem03.Senha;  
labelValues[12] = Triagem03.Local;  
labelValues[13] = Registro01.Senha;  
labelValues[14] = Registro01.Local;  
labelValues[15] = Registro02.Senha;  
labelValues[16] = Registro02.Local;  
labelValues[17] = Registro03.Senha;  
labelValues[18] = Registro03.Local;  
labelValues[19] = Medico01.Senha;  
labelValues[20] = Medico01.Local;  
labelValues[21] = Medico02.Senha;  
labelValues[22] = Medico02.Local;  
labelValues[23] = Medico03.Senha;  
labelValues[24] = Medico03.Local;  
labelValues[25] = Enfermagem01.Senha;  
labelValues[26] = Enfermagem01.Local;  
labelValues[27] = Enfermagem02.Senha;  
labelValues[28] = Enfermagem02.Local;  
labelValues[29] = Enfermagem03.Senha;  
labelValues[30] = Enfermagem03.Local;  
labelValues[31] = Exames01.Senha;  
labelValues[32] = Exames01.Local;  
labelValues[33] = Exames02.Senha;  
labelValues[34] = Exames02.Local;  
labelValues[35] = Exames03.Senha;  
labelValues[36] = Exames03.Local;  
labelValues[37] = NovaSenha ("T" ou "F");  
labelValues[38] = IDUnidadeAtendimento;  
labelValues[39] = ChamaVozPainel ("T" ou "F");  
labelValues[40] = SequencialSenha;

**Tamanho e cores**

Para alterar o tamanho e a cor de elementos em sua página ASPX, você deve fazer ajustes no arquivo CSS.

1. Abra o arquivo CSS associado à página ASPX, o arquivo está localizado na pasta no painel ..\css\styles.css
2. Localize a classe ou o ID do elemento que você deseja modificar. Se não houver, crie um.

   1. Por exemplo: `.nome-da-classe` ou `#nome-do-id`.
3. Dentro das chaves `{}` desse seletor, adicione ou ajuste as propriedades.
4. Salve o arquivo CSS e atualize a página no navegador para ver as mudanças
