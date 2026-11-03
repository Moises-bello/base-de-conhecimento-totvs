---
content_hash: 090a65accfcb083525dc413d7aa9450b667f24dd4ac7c22ba9b8b9fe09b10670
fetched_at: '2026-06-29T00:06:16.203827+00:00'
page_id: '211064766'
product: rm
source: tdn-rm
title: GLB0005_ESTOURO_DE_MEMORIA_NA_GERACAO_DE_UM_CUBO_NET
type: documentation
url: https://tdn.totvs.com/display/LRM/GLB0005_ESTOURO_DE_MEMORIA_NA_GERACAO_DE_UM_CUBO_NET
version: 22
---

# ESTOURO DE MEMORIA NA GERACAO DE UM CUBO NET

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.82.41, 11.82.42.XX |
| **Ocorrência:** | Estouro de Memória (SystemOutOfMemoryException) na Geração de um Cubo .Net |
| **Ambiente:** | Inteligência de Negócio (Cubo .Net) |
| **Passo a passo:** | ``` Na geração de um cubo .Net ou na exportação de um cubo para arquivo (.XLS, XLSX, CSV, TXT, [...] ) uma exceção de Estouro de Memória da Aplicação (SystemOuOfMemoryException) é levantado. ```  POSSÍVEIS CAUSAS:1) O **RM.exe** e/ou o **RM.Host.exe**\* podem estar sendo executados em 32 bits.  * ```    Ao se executar o RM.exe e/ou o RM.Host.exe* em 32 bits, reduz-se o limite de consumo de memória da aplicação, fazendo com que não haja espaço sequencial de memória suficiente para gerar um cubo com muitos registros. *RM.Host.exe (executável) ou RM.Host.Service.exe (serviço).   ```    ```       ```   **Imagem 1: O RM.Host.exe está sendo executado em 32 bits (Limita-se o espaço de memória suficiente para a geração correta do cubo)**  ```    Imagem 2: O RM.exe está sendo executado em 32 bits (Limita-se o espaço de memória suficiente para a geração correta do cubo)  ```   **Imagem 3: O RM.Host.exe está sendo executado em 64 bits (O cubo pode consumir a memória disponível em sua totalidade)**  ```   Imagem 4: O RM.exe está sendo executado em 64 bits (O cubo pode consumir a memória disponível em sua totalidade)  OBS: Para que o RM.exe e/ou RM.Host.exe sejam executados em 64 bits, abra o Prompt de Comando, apertando (Windows+R) e digitando "cmd";    ```  ```  Imagem 5: Windows+R -> Executar, digitar "cmd"   ```  ```  Imagem 6: Prompt de comando   ```  ``` Execute os comandos abaixo:   ```  ``` cd\ cd C:\totvs\CorporeRM\RM.Net CorFlags.exe RM.exe /32bit- CorFlags.exe RM.Host.exe /32bit- CorFlags.exe RM.Host.Service.exe /32bit-   ```  ``` O Resultado da execução dos comandos acima deve ser semelhante a esse:   Imagem 7: Resultado da execução dos comandos citados acima. ```  2) A Memória Física é insuficiente para a geração correta do cubo.  * ```   Foi evidenciado que uma máquina com memória menor ou igual a 4 gb é incapaz de gerar um cubo .net com muitos registros, é capaz de gerar apenas cubos com um número restrito de registros.    ``` * ```   Uma máquina com 8gb de memória é suficientemente capaz de gerar cubos com diversos registros, agrupamentos, filtros e outros componentes de tela.   ```  Dicas para a geração correta de um cubo .net:1) TAG DBSCommandTimeout  * ```   Caso a consulta SQL demore mais que 1m e 40s (DBSCommandTimeout = 60000)], deve-se aumentar esse número*, para que o tempo de resposta do banco de dados seja suficiente para que o mesmo possa processar a requisição   ```    ```   e traga os devidos dados.    ```    ```   *Sugerido: 1000000   ```    ```       ```   **Imagem 8: TAG DBSCommandTimeout = 1000000**Dicas para uma melhor performance de um cubo .net1) Sufixos \_N, \_S, \_D [...], em parâmetros da consulta sql vinculada ao cubo .Net  * ```   Ao adicionar sufixos aos parâmetros de uma consulta sql, o mecanismo de execução da consulta SQL, utiliza o tipo passado através do sufixo (_N: numérico, _S:string, D: data, [...]), fazendo com que a verificação interna de tipos,   ```    ```   não seja executada, fazendo com que a consulta seja retornada mais rapidamente.    ```    ```       ```   **Imagem 9: Sufixos em parâmetros da consulta SQL** |
| **Observações:** |  |
