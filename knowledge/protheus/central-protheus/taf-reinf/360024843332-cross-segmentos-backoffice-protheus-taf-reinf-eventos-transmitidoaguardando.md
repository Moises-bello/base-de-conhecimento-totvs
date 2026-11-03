---
article_id: 360024843332
category: TAF - REINF
content_hash: bd639386741e443dda1d29593e4d198ced3fe1965db3d2d20f9cc270da9b9824
fetched_at: '2026-06-28T22:41:34.674636+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Eventos Transmitido/Aguardando
type: support-article
updated_at: '2024-10-02T12:18:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024843332-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Eventos-Transmitido-Aguardando
---

**Ocorrência**

Ao transmitir algum evento da Reinf e monitorá-lo, não há retorno, permanecendo no status Transmitido/Aguardando.

**Ambiente**

TAF - A partir da 12.1.25

obs: ambientes anteriores a versão 12.1.25 do TSS não transmitem o Reinf.

**Causa**

As causas poderão ser diversas. Para uma melhor análise, recomendamos que na abertura de um chamado seja anexado o console.log e o appserver.ini do TSS, após o monitoramento do evento pendente. Entretanto, será abordado abaixo algumas causas do problema:

**Solução**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048044713)**

* TSS não estar na versão 3.0;
* Certificado Digital vencido ou não configurado na Wizard TSS do TAF;
* Falta de atualização das URLs do TSS;
* Appserver.ini com alguma inconsistência.
* Evento em Processamento.
* Monitoramento dos eventos sendo feita fora da matriz onde foi transmitida.

A primeira coisa a analisar, é verificar como está o STATUS do evento transmitido na tabela SPED500. Para acessar a tabela SPED500, abra o Smartclient do TSS. (pasta de instalação do TSS bin/smartclient/smartclient.exe). Siga o caminho abaixo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048060973)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048061213)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048061653)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048061793)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047179334)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047179634)

Existe algumas possíveis situações:

Quando o evento foi transmitido, **não é identificado** no portal da Receita por estar com os status: Status 2 ou 4 - Evento Recebido.

Quando o evento foi transmitido, **é identificado** no portal da Receita mas não retornou para o TAF: Status 3, 5 ou 6 - Inconsistente, Rejeitado ou Autorizado.

Caso os eventos estiverem com status 2 ou 4, avalie a **parte 1** do artigo. Caso os eventos estejam como 3, 5 ou 6, avalie a **parte 2** do artigo.

**Parte 1 - Status 2 ou 4**

**1. TSS na versão 3.0.**

Caso o TSS não esteja na versão 3.0, não será possível transmitir e/ou Receber o retorno dos Eventos.

Verifique no artigo abaixo:

[TAF - REINF- Como identificar se o TSS está habilitado para utilizar a Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022075612-TAF-REINF-Como-identificar-se-o-TSS-est%C3%A1-habilitado-para-utilizar-a-Reinf?source=search)

**2. Certificado Digital vencido ou não configurado na Wizard TSS do TAF.**

Para que a transmissão e o retorno ocorram sem problemas, o certificado digital deverá ser configurado conforme abaixo:

Certificado A1: [TAF - ESOCIAL/REINF- Como configurar o certificado digital modelo A1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022254351-TAF-ESOCIAL-REINF-Como-configurar-o-certificado-digital-modelo-A1?source=search)

Certificado A3: [TSS - Certificado A3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018849891-TSS-Certificado-A3?source=search)

**3. Falta de Atualização das URLs do TSS.**

Geralmente, quando há problema referente a URL de transmissão, no console.log do TSS é gerado um erro com a seguinte estrutura:

**WSCERRXXX - Retorno VAZIO de POST - (URL utilizada) - Http 404 Not Found**

Para correção, é necessário atualizar as URLs conforme artigo abaixo:

[TSS - Atualização das URLs do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025394911-TSS-Atualiza%C3%A7%C3%A3o-das-URLs-do-TSS?source=search)

**4. Appserver.ini com alguma inconsistência.**

Caso o Appserver.ini do TSS esteja com alguma inconsistência - Jobs comentados, falta de alguma seção obrigatória - a transmissão poderá ser comprometida. Os itens principais a se avaliar:

Seção [SPED]

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048048733)

JOBS - não podem estar comentados ou inexistentes. A configuração da linha INSTANCES irá depender de cada ambiente, mas o formato precisa estar dessa maneira: Instances= n, n, n, n. Para mais informações sobre essa linha, verifique: <https://tdn.totvs.com/display/tec/Instances>

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048048873)

Segue artigo explicativo sobre os JOBS: [TSS - Funcionalidades dos JOBs do TSS 3.0](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018584232-TSS-Funcionalidades-dos-JOBs-do-TSS-3-0?source=search)

Seção [ONSTART] - os JOBS acima precisam estar na linha JOBS e a linha REFRESHRATE também é obrigatória, caso apague ou comente essas linhas o TSS não irá transmitir os eventos.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048048993)

Seção [SSLCONFIGURE] - Obrigatório os itens SSL2, SSL3, TLS1\_0, TLS\_1 e TLS\_2 estarem conforme abaixo.

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048064193)

**5.Evento em Processamento**

Se o evento sem retorno tratar-se do R-2099 e o mesmo estiver como "Em processamento", avalie o link a seguir: [R-2099 Em Processamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016032791-R-2099-Em-Processamento?source=search)

**5.Bloqueio da URL de transmissão da RFB.**

Foi alterada a URL de transmissão da RFB, ambiente com alta proteção de firewall deve realizar o desbloqueio da URL para envio e retorno das informações.

Copie a URL abaixo no seu navegador e caso retorne com erro realize o desbloqueio da URL:

<https://reinf.receita.economia.gov.br/>"

**Parte 2 - Status 3, 5 ou 6**

Neste caso, o TSS está falhando em retornar para o TAF os eventos.

**1. Avaliar a URL na Wizard do TSS.**

Uma das causas deste problema é o ambiente TAF estar apontando para um TSS, sendo que o TSS ativo é outro; isso geralmente ocorre quando há duas ou mais instalações do TSS.

Neste caso, avalie se o endereço e a porta estão corretos.

**2. Erros no Console.log.**

Caso esteja ocorrendo erros no Console do TSS, realize a abertura de um chamado Junto a Equipe TOTVS anexando o Console.log para análise.

**3. Monitoramento dos eventos sendo feita fora da matriz onde foi transmitida.**

Supondo que haja duas empresas, 01 e 02. Se a transmissão de um evento foi feito pela matriz 0101, o monitoramento precisa ser realizado acessando o ambiente pela matriz 0101, caso contrário, o monitoramento não será realizado.
