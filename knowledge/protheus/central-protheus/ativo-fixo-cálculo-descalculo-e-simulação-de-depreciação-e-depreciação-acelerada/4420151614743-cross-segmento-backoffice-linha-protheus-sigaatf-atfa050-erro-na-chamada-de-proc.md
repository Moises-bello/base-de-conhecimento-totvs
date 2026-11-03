---
article_id: 4420151614743
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: bbc844f3d3bcdeebe2fe9b0392a21de4c64173b0c18d7c956f7dfe0480c061d7
fetched_at: '2026-06-28T22:41:43.252061+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA050 - Erro na chamada
  de processo.
type: support-article
updated_at: '2026-01-13T13:02:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420151614743-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Erro-na-chamada-de-processo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16026397799447) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
  
No módulo ativo fixo, ao tentar realizar a rotina ATFA050 Cálculo da Depreciação, sistema apresenta a mensagem:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420144688279)**

**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo - Todas as versões  
  
  
**Causa**  
O incidente pode ocorrer devido a:

1. **Incompatibilidade de Assinaturas:** A rotina (Fonte/RPO) possui uma assinatura diferente da Procedure instalada no banco ou do pacote disponível no RPO.
2. **Pacote ZSPS Desatualizado no RPO:** O arquivo `.ZSPS` embarcado no RPO é antigo e não contém as correções necessárias.
3. **Conflito de Customização:** Pontos de Entrada (PEs) nas procedures impedindo a atualização correta.

**Solução**   
O processo de atualização de procedures não utiliza mais arquivos físicos `.SPS`. A correção deve ser realizada via **Configurador (SIGACFG)** utilizando os pacotes `.ZSPS` contidos no RPO ou baixados via Central de Atualizações.

Realize os passos abaixo:

**1. Atualização do RPO (Pacotes ZSPS)** Para garantir que o instalador tenha os arquivos corretos, é necessário aplicar o pacote de **Expedição Contínua** do módulo (neste caso, Ativo Fixo/Backoffice).

* Baixe e aplique o Patch mais recente do módulo no RPO. Isso atualizará os arquivos `.ZSPS` embarcados.
* Certifique-se de aplicar também a *Lib* mais recente para atualizar a rotina gerenciadora `CFGX051M`.

**2. Procedimento de Atualização (Novo Gerenciador)**

1. Acesse o **Configurador (SIGACFG)** em modo exclusivo.
2. Caminho: **Base de Dados > Dicionário > Stored Procedure** (Rotina CFGX051M).
3. O sistema exibirá a lista de processos (Procedures) e o status de cada um (ex: Desatualizado, Incompatível, Atualizado).
4. Selecione a empresa e o processo referente ao **Ativo Fixo** (ex: Procedure 11).
5. Verifique na coluna de detalhes se o **IDSPS** do RPO (ou TPH se estiver online) é superior ao Instalado.
6. Clique no botão **Instalar** (ícone de seta/download na lateral).
7. Aguarde a mensagem de "Sucesso" no log de processamento.

**3. Tratativa para Pontos de Entrada (Parâmetro MV\_DROPPE)** Se houver falha na instalação ou suspeita de PEs corrompidos, é necessário forçar a remoção dos mesmos.

> **Importante**: O procedimento a seguir é crítico. O parâmetro `MV_DROPPE` força a exclusão dos Pontos de Entrada associados às Stored Procedures. Como o controle dessas customizações é de responsabilidade do cliente, o Suporte Padrão não mensura o impacto funcional da remoção.

1. Realize **Backup** completo do Banco de Dados.
2. No Configurador, altere o parâmetro **MV\_DROPPE** para **.T.** (True).
3. Acesse novamente o Gerenciador de Procedures (`CFGX051M`).
4. Selecione a procedure e clique em **Desinstalar** (ícone de lixeira).
5. Após a conclusão, clique em **Instalar** novamente.
6. Retorne o parâmetro `MV_DROPPE` para **.F.** (False).

**4. Solução de Contorno: Forçar Pacotes do RPO (Modo Offline)** Caso a Central de Atualizações não esteja acessível ou apresente erro, você pode forçar o uso do pacote interno do RPO:

1. Na tela do gerenciador, clique em **Configurações Adicionais** (ícone de engrenagem).
2. Marque a opção: **Forçar utilização de pacotes .ZSPS contidos no RPO**.
3. Prossiga com a instalação.

**Saiba Mais**  
[Stored Procedures - Novo gerenciador de pacotes](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes)
